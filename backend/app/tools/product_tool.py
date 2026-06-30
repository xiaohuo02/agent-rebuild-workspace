from app.tools.schemas import Evidence, ToolResult, ToolStatus


PRODUCTS = {
    "智能门锁": {
        "price": "1299 元",
        "stock": "现货 23 件",
        "feature": "支持指纹、密码和临时授权开门",
    },
    "智能音箱": {
        "price": "399 元",
        "stock": "现货 58 件",
        "feature": "支持语音控制和蓝牙播放",
    },
}


def query_product(task: str) -> ToolResult:
    matched_name = next((name for name in PRODUCTS if name in task), None)
    if not matched_name:
        return ToolResult(
            tool="product_tool",
            status=ToolStatus.EMPTY,
            summary="没有匹配到商品。",
        )

    product = PRODUCTS[matched_name]
    content = (
        f"{matched_name}：价格 {product['price']}，库存 {product['stock']}，"
        f"特点：{product['feature']}。"
    )
    return ToolResult(
        tool="product_tool",
        status=ToolStatus.SUCCESS,
        summary=content,
        evidence=[
            Evidence(
                source="fake_product_catalog",
                title=f"{matched_name} 商品信息",
                content=content,
                metadata={"product": matched_name},
            )
        ],
    )
