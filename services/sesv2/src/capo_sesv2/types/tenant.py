"""Generated from Smithy shape ``com.amazonaws.sesv2#Tenant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.sending_status
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.tenant_id
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.tenant_suppression_attributes
    import capo_sesv2.types.timestamp


class Tenant(TypedDict, closed=True):
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant.</p>"""
    tenant_id: NotRequired["capo_sesv2.types.tenant_id.TenantId"]
    """<p>A unique identifier for the tenant.</p>"""
    tenant_arn: NotRequired["capo_sesv2.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the tenant.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the tenant was created.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) associated with the tenant.</p>"""
    sending_status: NotRequired["capo_sesv2.types.sending_status.SendingStatus"]
    """<p>The status of sending capability for the tenant:</p> <ul> <li> <p> <code>ENABLED</code> – Sending is allowed for the tenant.</p> </li> <li> <p> <code>DISABLED</code> – Sending is prevented for the tenant.</p> </li> <li> <p> <code>REINSTATED</code> – Sending is allowed even if there are active reputation findings.</p> </li> </ul>"""
    suppression_attributes: NotRequired[
        "capo_sesv2.types.tenant_suppression_attributes.TenantSuppressionAttributes"
    ]
    """<p>An object that contains information about the suppression list preferences for the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tenant) -> dict:
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
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "sending_status" in value:
        import capo_sesv2.types.sending_status

        out["SendingStatus"] = capo_sesv2.types.sending_status.serialize_json(
            value["sending_status"]
        )
    if "suppression_attributes" in value:
        import capo_sesv2.types.tenant_suppression_attributes

        out["SuppressionAttributes"] = (
            capo_sesv2.types.tenant_suppression_attributes.serialize_json(
                value["suppression_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> Tenant:
    out: Tenant = {}  # type: ignore[typeddict-item]
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
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if data.get("SendingStatus") is not None:
        import capo_sesv2.types.sending_status

        out["sending_status"] = capo_sesv2.types.sending_status.deserialize_json(
            data["SendingStatus"]
        )
    if data.get("SuppressionAttributes") is not None:
        import capo_sesv2.types.tenant_suppression_attributes

        out["suppression_attributes"] = (
            capo_sesv2.types.tenant_suppression_attributes.deserialize_json(
                data["SuppressionAttributes"]
            )
        )
    return out
