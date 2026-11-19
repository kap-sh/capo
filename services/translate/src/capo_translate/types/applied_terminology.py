"""Generated from Smithy shape ``com.amazonaws.translate#AppliedTerminology``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.resource_name
    import capo_translate.types.term_list


class AppliedTerminology(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The name of the custom terminology applied to the input text by Amazon Translate for the translated text response.</p>"""
    terms: NotRequired["capo_translate.types.term_list.TermList"]
    """<p>The specific terms of the custom terminology applied to the input text by Amazon Translate for the translated text response. A maximum of 250 terms will be returned, and the specific terms applied will be the first 250 terms in the source text. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppliedTerminology) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "terms" in value:
        import capo_translate.types.term_list

        out["Terms"] = capo_translate.types.term_list.serialize_aws_json_1_1(
            value["terms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppliedTerminology:
    out: AppliedTerminology = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Terms") is not None:
        import capo_translate.types.term_list

        out["terms"] = capo_translate.types.term_list.deserialize_aws_json_1_1(
            data["Terms"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppliedTerminology) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "terms" in value:
        import capo_translate.types.term_list

        out["Terms"] = capo_translate.types.term_list.serialize_cbor(value["terms"])
    return out


def deserialize_cbor(data: dict) -> AppliedTerminology:
    out: AppliedTerminology = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Terms") is not None:
        import capo_translate.types.term_list

        out["terms"] = capo_translate.types.term_list.deserialize_cbor(data["Terms"])
    return out
