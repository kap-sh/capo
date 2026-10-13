"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListUploadsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.uploads


class ListUploadsResult(TypedDict, closed=True):
    uploads: NotRequired["capo_device_farm.types.uploads.Uploads"]
    """<p>Information about the uploads.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUploadsResult) -> dict:
    out: dict = {}
    if "uploads" in value:
        import capo_device_farm.types.uploads

        out["uploads"] = capo_device_farm.types.uploads.serialize_aws_json_1_1(
            value["uploads"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUploadsResult:
    out: ListUploadsResult = {}  # type: ignore[typeddict-item]
    if data.get("uploads") is not None:
        import capo_device_farm.types.uploads

        out["uploads"] = capo_device_farm.types.uploads.deserialize_aws_json_1_1(
            data["uploads"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListUploadsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "uploads" in value:
        import capo_device_farm.types.uploads

        out["uploads"] = capo_device_farm.types.uploads.redact_sensitive(
            value["uploads"]
        )
    return out
