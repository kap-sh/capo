"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.sending_status
    import capo_sesv2.types.tenant_id
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.timestamp


class TenantInfo(TypedDict, closed=True):
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant.</p>"""
    tenant_id: NotRequired["capo_sesv2.types.tenant_id.TenantId"]
    """<p>A unique identifier for the tenant.</p>"""
    tenant_arn: NotRequired["capo_sesv2.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the tenant.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the tenant was created.</p>"""
    sending_status: NotRequired["capo_sesv2.types.sending_status.SendingStatus"]
    """<p>The status of sending capability for the tenant:</p> <ul> <li> <p> <code>ENABLED</code> – Sending is allowed for the tenant.</p> </li> <li> <p> <code>DISABLED</code> – Sending is prevented for the tenant.</p> </li> <li> <p> <code>REINSTATED</code> – Sending is allowed even if there are active reputation findings.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenantInfo) -> dict:
    out: dict = {}
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "tenant_arn" in value:
        out["TenantArn"] = value["tenant_arn"]
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "sending_status" in value:
        import capo_sesv2.types.sending_status

        out["SendingStatus"] = capo_sesv2.types.sending_status.serialize_json(
            value["sending_status"]
        )
    return out


def deserialize_json(data: dict) -> TenantInfo:
    out: TenantInfo = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("TenantArn") is not None:
        out["tenant_arn"] = data["TenantArn"]
    if data.get("CreatedTimestamp") is not None:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("SendingStatus") is not None:
        import capo_sesv2.types.sending_status

        out["sending_status"] = capo_sesv2.types.sending_status.deserialize_json(
            data["SendingStatus"]
        )
    return out
