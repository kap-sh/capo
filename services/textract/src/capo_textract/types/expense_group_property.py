"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseGroupProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.string
    import capo_textract.types.string_list


class ExpenseGroupProperty(TypedDict, closed=True):
    types: NotRequired["capo_textract.types.string_list.StringList"]
    """<p>Informs you on whether the expense group is a name or an address.</p>"""
    id: NotRequired["capo_textract.types.string.String"]
    """<p>Provides a group Id number, which will be the same for each in the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseGroupProperty) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_textract.types.string_list

        out["Types"] = capo_textract.types.string_list.serialize_aws_json_1_1(
            value["types"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseGroupProperty:
    out: ExpenseGroupProperty = {}  # type: ignore[typeddict-item]
    if data.get("Types") is not None:
        import capo_textract.types.string_list

        out["types"] = capo_textract.types.string_list.deserialize_aws_json_1_1(
            data["Types"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseGroupProperty) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_textract.types.string_list

        out["Types"] = capo_textract.types.string_list.serialize_cbor(value["types"])
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_cbor(data: dict) -> ExpenseGroupProperty:
    out: ExpenseGroupProperty = {}  # type: ignore[typeddict-item]
    if data.get("Types") is not None:
        import capo_textract.types.string_list

        out["types"] = capo_textract.types.string_list.deserialize_cbor(data["Types"])
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
