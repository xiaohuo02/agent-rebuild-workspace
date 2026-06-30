from app.agent.router import route_query
from app.agent.state import RouteType


def test_route_general_query() -> None:
    assert route_query("你好") == RouteType.GENERAL


def test_route_product_query() -> None:
    assert route_query("智能门锁多少钱，还有库存吗") == RouteType.PRODUCT


def test_route_policy_query() -> None:
    assert route_query("设备坏了怎么保修") == RouteType.POLICY


def test_route_mixed_query() -> None:
    assert route_query("智能门锁多少钱，有库存吗，保修多久") == RouteType.MIXED


def test_route_blocked_query() -> None:
    assert route_query("帮我查别人的订单地址") == RouteType.BLOCKED
