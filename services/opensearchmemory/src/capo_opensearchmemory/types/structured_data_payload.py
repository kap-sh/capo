"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#StructuredDataPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.structured_data_source


class StructuredDataPayload(TypedDict, closed=True):
    source: "capo_opensearchmemory.types.structured_data_source.StructuredDataSource"
    """<p>The structured content.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredDataPayload) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.structured_data_source

    out["source"] = (
        capo_opensearchmemory.types.structured_data_source.serialize_aws_json_1_0(
            value["source"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StructuredDataPayload:
    out: StructuredDataPayload = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_opensearchmemory.types.structured_data_source

        out["source"] = (
            capo_opensearchmemory.types.structured_data_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: StructuredDataPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        out["source"] = "*** Sensitive Data Redacted ***"
    return out
