from app.agent.state import RouteType


BLOCKED_KEYWORDS = ("别人的订单", "泄露", "系统提示词", "绕过规则")
PRODUCT_KEYWORDS = ("价格", "库存", "有货", "多少钱", "商品", "门锁", "音箱")
POLICY_KEYWORDS = ("保修", "退货", "换货", "售后", "坏了", "维修")


def route_query(query: str) -> RouteType:
    if any(keyword in query for keyword in BLOCKED_KEYWORDS):
        return RouteType.BLOCKED

    has_product = any(keyword in query for keyword in PRODUCT_KEYWORDS)
    has_policy = any(keyword in query for keyword in POLICY_KEYWORDS)

    if has_product and has_policy:
        return RouteType.MIXED
    if has_product:
        return RouteType.PRODUCT
    if has_policy:
        return RouteType.POLICY
    return RouteType.GENERAL
