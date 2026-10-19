"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditSuppressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.resource_identifier


class DescribeAuditSuppressionRequest(TypedDict, closed=True):
    check_name: "capo_iot.types.audit_check_name.AuditCheckName"
    resource_identifier: "capo_iot.types.resource_identifier.ResourceIdentifier"


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditSuppressionRequest) -> dict:
    out: dict = {}
    out["checkName"] = value["check_name"]
    import capo_iot.types.resource_identifier

    out["resourceIdentifier"] = capo_iot.types.resource_identifier.serialize_json(
        value["resource_identifier"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAuditSuppressionRequest:
    out: DescribeAuditSuppressionRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkName") is not None:
        out["check_name"] = data["checkName"]
    else:
        out["check_name"] = ""
    if data.get("resourceIdentifier") is not None:
        import capo_iot.types.resource_identifier

        out["resource_identifier"] = (
            capo_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAuditSuppressionRequest.resource_identifier required"
        )
    return out
