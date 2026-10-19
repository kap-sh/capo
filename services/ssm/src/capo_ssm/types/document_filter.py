"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_filter_key
    import capo_ssm.types.document_filter_value


class DocumentFilter(TypedDict, closed=True):
    key: "capo_ssm.types.document_filter_key.DocumentFilterKey"
    """<p>The name of the filter.</p>"""
    value: "capo_ssm.types.document_filter_value.DocumentFilterValue"
    """<p>The value of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.document_filter_key

    out["key"] = capo_ssm.types.document_filter_key.serialize_aws_json_1_1(value["key"])
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentFilter:
    out: DocumentFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_ssm.types.document_filter_key

        out["key"] = capo_ssm.types.document_filter_key.deserialize_aws_json_1_1(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.document_filter_key.DocumentFilterKey", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
