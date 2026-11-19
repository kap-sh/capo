"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateSubdomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.operation
    import capo_lightsail.types.subdomain


class CreateSubdomainResult(TypedDict, closed=True):
    subdomain: NotRequired["capo_lightsail.types.subdomain.Subdomain"]
    """<p>An object that describes the subdomain that was created.</p>"""
    operation: NotRequired["capo_lightsail.types.operation.Operation"]
    """<p>An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubdomainResult) -> dict:
    out: dict = {}
    if "subdomain" in value:
        import capo_lightsail.types.subdomain

        out["subdomain"] = capo_lightsail.types.subdomain.serialize_aws_json_1_1(
            value["subdomain"]
        )
    if "operation" in value:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubdomainResult:
    out: CreateSubdomainResult = {}  # type: ignore[typeddict-item]
    if data.get("subdomain") is not None:
        import capo_lightsail.types.subdomain

        out["subdomain"] = capo_lightsail.types.subdomain.deserialize_aws_json_1_1(
            data["subdomain"]
        )
    if data.get("operation") is not None:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
