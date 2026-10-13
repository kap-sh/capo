"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.template


class DescribeTemplateResponse(TypedDict, closed=True):
    template: NotRequired["capo_quicksight.types.template.Template"]
    """<p>The template structure for the object you want to describe.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplateResponse) -> dict:
    out: dict = {}
    if "template" in value:
        import capo_quicksight.types.template

        out["Template"] = capo_quicksight.types.template.serialize_json(
            value["template"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTemplateResponse:
    out: DescribeTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Template") is not None:
        import capo_quicksight.types.template

        out["template"] = capo_quicksight.types.template.deserialize_json(
            data["Template"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeTemplateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        import capo_quicksight.types.template

        out["template"] = capo_quicksight.types.template.redact_sensitive(
            value["template"]
        )
    return out
