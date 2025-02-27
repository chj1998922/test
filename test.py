addr_label = ["TOWN", "ROAD", "OFFICE", "COMM", "VILLAGE"]
address_ner = "山西省/PROVINCE###长治市/CITY###武乡县/COUNTY###洪水村/VILLAGE###吃啥路/ROAD###12号/STREETNO###次撒社区/COMM"

# 初始化一个空列表，用于存储匹配的地址
matched_addresses = []

# 将 address_ner 按 ### 分割成多个地址项
address_items = address_ner.split("###")

i = 0
while i < len(address_items):
    item = address_items[i]
    # 按 / 分割出地址和对应的标签
    address, label = item.split("/")

    if label == "ROAD":
        # 先把 ROAD 单独添加
        matched_addresses.append(address)
        if i + 1 < len(address_items):
            next_item = address_items[i + 1]
            next_address, next_label = next_item.split("/")
            if next_label == "STREETNO":
                # 如果当前标签是 ROAD 且下一个标签是 STREETNO，合并两个地址
                combined_address = address + next_address
                matched_addresses.append(combined_address)
                i += 1  # 跳过下一个已处理的项

    elif label in addr_label:
        # 如果标签在 addr_label 列表中，添加该地址
        matched_addresses.append(address)

    i += 1

print("包含指定标签的地址有:", matched_addresses)