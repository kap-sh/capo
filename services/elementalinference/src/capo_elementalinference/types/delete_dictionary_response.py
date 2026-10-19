"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteDictionaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_arn
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_status


class DeleteDictionaryResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.dictionary_arn.DictionaryArn"
    """<p>The ARN of the deleted dictionary.</p>"""
    id: "capo_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the deleted dictionary.</p>"""
    status: "capo_elementalinference.types.dictionary_status.DictionaryStatus"
    """<p>The status of the dictionary after deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDictionaryResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_elementalinference.types.dictionary_status

    out["status"] = capo_elementalinference.types.dictionary_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDictionaryResponse:
    out: DeleteDictionaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        import capo_elementalinference.types.dictionary_status

        out["status"] = (
            capo_elementalinference.types.dictionary_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.dictionary_status.DictionaryStatus", ""
        )
    return out
