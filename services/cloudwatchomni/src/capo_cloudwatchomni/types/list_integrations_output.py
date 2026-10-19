"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListIntegrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_list


class ListIntegrationsOutput(TypedDict, closed=True):
    items: "capo_cloudwatchomni.types.integration_list.IntegrationList"
    """The page of integrations."""
    next_token: NotRequired["str"]
    """Pagination token for the next page; absent when there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListIntegrationsOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.integration_list

    out["items"] = capo_cloudwatchomni.types.integration_list.serialize_cbor(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListIntegrationsOutput:
    out: ListIntegrationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_cloudwatchomni.types.integration_list

        out["items"] = capo_cloudwatchomni.types.integration_list.deserialize_cbor(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
