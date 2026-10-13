"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetListElementsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.elements_list
    import capo_frauddetector.types.next_token


class GetListElementsResult(TypedDict, closed=True):
    elements: NotRequired["capo_frauddetector.types.elements_list.ElementsList"]
    """<p> The list elements. </p>"""
    next_token: NotRequired["capo_frauddetector.types.next_token.nextToken"]
    """<p> The next page token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetListElementsResult) -> dict:
    out: dict = {}
    if "elements" in value:
        import capo_frauddetector.types.elements_list

        out["elements"] = capo_frauddetector.types.elements_list.serialize_aws_json_1_1(
            value["elements"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetListElementsResult:
    out: GetListElementsResult = {}  # type: ignore[typeddict-item]
    if data.get("elements") is not None:
        import capo_frauddetector.types.elements_list

        out["elements"] = (
            capo_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetListElementsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "elements" in value:
        import capo_frauddetector.types.elements_list

        out["elements"] = capo_frauddetector.types.elements_list.redact_sensitive(
            value["elements"]
        )
    return out
