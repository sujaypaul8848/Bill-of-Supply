## Kinara LMS

LMS for Kinara Capital

#### License

MIT


def put_purchase_receipt():
    if frappe.request.method == "PUT":
        data = json.loads(frappe.request.data)
        print(data)
        try:
            if frappe.db.exists("Purchase Receipt", data['name']):
                items = frappe.get_doc('Purchase Receipt', data['name'])
                # Ensure Karigar exists
                if not frappe.db.exists("Karigar", data['custom_karigar']):
                    doc = frappe.get_doc({
                        'doctype': 'Karigar',
                        'karigar_name': data["custom_karigar"],
                    })
                    doc.insert(ignore_permissions=True)
                items.custom_karigar = data['custom_karigar']
                items.remarks = data['remarks']
                items.custom_ready_receipt_type = data['custom_ready_receipt_type']
                for row in data["items"]:
                    if not row["idx"]:
                        frappe.throw("Please Enter a valid idx")
                    # Ensure Item exists
                    if not frappe.db.exists("Item", row['product_code']):
                        new_product = frappe.get_doc({
                            'doctype': 'Item',
                            'item_code': row['product_code'],
                            'item_group': row['item_group'],
                        })
                        new_product.insert(ignore_permissions=True)
                    # recFound = False
                    rec = next((item for item in items.items.idx == idx.get("idx")), None)
                    for rec in items.items:
                        existing_child_entry = next((child for child in var.purchase_receipt_item_breakup_detail if child.idx == i.get("idx")), None)
                        if rec.idx == row["idx"]:
                            # recFound = True
                            rec.item_code = row.get("product_code", "")
                            rec.item_group = row.get("item_group", "")
                            rec.custom_kun_karigar = row.get("custom_kun_karigar", "")
                            rec.custom_net_wt = row.get("custom_net_wt", 0.0)
                            rec.custom_few_wt = row.get("custom_few_wt", 0.0)
                            rec.custom_gross_wt = row.get("custom_gross_wt", 0.0)
                            rec.custom_mat_wt = row.get("custom_mat_wt", 0.0)
                            rec.custom_other = row.get("custom_other", 0.0)
                            rec.custom_total = row.get("custom_total", 0.0)
                            rec.custom_add_photo = row.get("custom_add_photo")
                            rec.custom_purchase_receipt_item_breakup = row.get("custom_purchase_receipt_item_breakup")
                            # Process nested table
                            if rec.custom_purchase_receipt_item_breakup:
                                var = frappe.get_doc("Purchase Receipt Item Breakup", rec.custom_purchase_receipt_item_breakup)
                                child_var = frappe.get_all("Purchase Receipt Item Breakup Detail", filters={"parent": var.name})
                                table = row.get("table", [])
                                for i in table:
                                    # if i.get("idx") == row["idx"]:
                                        # Update or add child table entries
                                        material_name = i.get("material")
                                        if not frappe.db.exists("Material", material_name):
                                            new_material = frappe.get_doc({
                                                'doctype': 'Material',
                                                'material_name': material_name,
                                            })
                                            new_material.insert(ignore_permissions=True)
                                        child_entry = {
                                            "doctype": "Purchase Receipt Item Breakup Detail",
                                            "material_abbr": i.get('material_abbr'),
                                            "material": material_name,
                                            "pcs": i.get("pcs"),
                                            "piece_": i.get("piece_"),
                                            "carat": i.get("carat"),
                                            "carat_": i.get("carat_"),
                                            "weight": i.get("weight"),
                                            "gm_": i.get("gm_"),
                                            "amount": i.get("amount")
                                        }
                                        # Find existing child entry
                                        existing_child_entry = next((child for child in var.purchase_receipt_item_breakup_detail if child.idx == i.get("idx")), None)
                                        if existing_child_entry:
                                            # Update existing entry
                                            existing_child_entry.update(child_entry)
                                        else:
                                            # Add new entry
                                            var.append("purchase_receipt_item_breakup_detail", child_entry)
                                var.save()
                                print(var)
                                print(child_var)
                            break
                    # if not recFound:
                    #     frappe.throw("Please Enter a valid idx")
                items.save()
                return build_response("success", data="okay")
            else:
                return build_response("error", message="No such record exists")
        except Exception as e:
            frappe.db.rollback()
            frappe.logger("Put Purchase Receipt").exception(e)
            frappe.log_error(title=_("API Error"), message=e)
            return build_response("error", message=str(e))