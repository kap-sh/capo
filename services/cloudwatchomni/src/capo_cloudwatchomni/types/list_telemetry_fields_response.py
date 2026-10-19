"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListTelemetryFieldsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.field_list


class ListTelemetryFieldsResponse(TypedDict, closed=True):
    fields: "capo_cloudwatchomni.types.field_list.FieldList"
    """The list of fields available for queries."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTelemetryFieldsResponse) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.field_list

    out["fields"] = capo_cloudwatchomni.types.field_list.serialize_cbor(value["fields"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTelemetryFieldsResponse:
    out: ListTelemetryFieldsResponse = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_cloudwatchomni.types.field_list

        out["fields"] = capo_cloudwatchomni.types.field_list.deserialize_cbor(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
