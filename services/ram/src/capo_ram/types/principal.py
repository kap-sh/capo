"""Generated from Smithy shape ``com.amazonaws.ram#Principal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.boolean
    import capo_ram.types.date_time
    import capo_ram.types.string


class Principal(TypedDict, closed=True):
    id: NotRequired["capo_ram.types.string.String"]
    """<p>The ID of the principal that can be associated with a resource share.</p>"""
    resource_share_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of a resource share the principal is associated with.</p>"""
    creation_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when the principal was associated with the resource share.</p>"""
    last_updated_time: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when the association between the resource share and the principal was last updated.</p>"""
    external: NotRequired["capo_ram.types.boolean.Boolean"]
    """<p>Indicates the relationship between the Amazon Web Services account the principal belongs to and the account that owns the resource share:</p> <ul> <li> <p> <code>True</code> – The two accounts belong to same organization.</p> </li> <li> <p> <code>False</code> – The two accounts do not belong to the same organization.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "creation_time" in value:
        import capo_ram.types.date_time

        out["creationTime"] = capo_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_ram.types.date_time

        out["lastUpdatedTime"] = capo_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "external" in value:
        out["external"] = value["external"]
    return out


def deserialize_json(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("creationTime") is not None:
        import capo_ram.types.date_time

        out["creation_time"] = capo_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_ram.types.date_time

        out["last_updated_time"] = capo_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if data.get("external") is not None:
        out["external"] = data["external"]
    return out
