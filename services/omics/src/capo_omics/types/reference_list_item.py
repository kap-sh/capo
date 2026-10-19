"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.md5
    import capo_omics.types.reference_arn
    import capo_omics.types.reference_description
    import capo_omics.types.reference_id
    import capo_omics.types.reference_name
    import capo_omics.types.reference_status
    import capo_omics.types.reference_store_id


class ReferenceListItem(TypedDict, closed=True):
    id: "capo_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    arn: "capo_omics.types.reference_arn.ReferenceArn"
    """<p>The reference's ARN.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's store ID.</p>"""
    md5: "capo_omics.types.md5.Md5"
    """<p>The reference's MD5 checksum.</p>"""
    status: NotRequired["capo_omics.types.reference_status.ReferenceStatus"]
    """<p>The reference's status.</p>"""
    name: NotRequired["capo_omics.types.reference_name.ReferenceName"]
    """<p>The reference's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The reference's description.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the reference was created.</p>"""
    update_time: "datetime.datetime"
    """<p>When the reference was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceListItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["md5"] = value["md5"]
    if "status" in value:
        out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    import capo_omics._protocol.serialize

    out["updateTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ReferenceListItem:
    out: ReferenceListItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("referenceStoreId") is not None:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        out["reference_store_id"] = ""
    if data.get("md5") is not None:
        out["md5"] = data["md5"]
    else:
        out["md5"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
