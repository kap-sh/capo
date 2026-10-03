"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Matcher``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.grpc_code
    import capo_elastic_load_balancing_v2.types.http_code


class Matcher(TypedDict, closed=True):
    http_code: NotRequired["capo_elastic_load_balancing_v2.types.http_code.HttpCode"]
    """<p>For Application Load Balancers, you can specify values between 200 and 499, with the default value being 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").</p> <p>For Network Load Balancers, you can specify values between 200 and 599, with the default value being 200-399. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").</p> <p>For Gateway Load Balancers, this must be "200–399".</p> <p>Note that when using shorthand syntax, some values such as commas need to be escaped.</p>"""
    grpc_code: NotRequired["capo_elastic_load_balancing_v2.types.grpc_code.GrpcCode"]
    """<p>You can specify values between 0 and 99. You can specify multiple values (for example, "0,1") or a range of values (for example, "0-5"). The default value is 12.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Matcher, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_code" in value:
        pairs.append((f"{key_prefix}HttpCode", str(value["http_code"])))
    if "grpc_code" in value:
        pairs.append((f"{key_prefix}GrpcCode", str(value["grpc_code"])))


def deserialize_query(el: Element) -> Matcher:
    out: Matcher = {}  # type: ignore[typeddict-item]
    child_http_code = el.find("HttpCode")
    if child_http_code is not None:
        out["http_code"] = str(child_http_code.text or "")
    child_grpc_code = el.find("GrpcCode")
    if child_grpc_code is not None:
        out["grpc_code"] = str(child_grpc_code.text or "")
    return out
