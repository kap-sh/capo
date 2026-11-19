"""Generated from Smithy shape ``com.amazonaws.textract#LendingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.document_group_list
    import capo_textract.types.undetected_document_type_list


class LendingSummary(TypedDict, closed=True):
    document_groups: NotRequired[
        "capo_textract.types.document_group_list.DocumentGroupList"
    ]
    """<p>Contains an array of all DocumentGroup objects.</p>"""
    undetected_document_types: NotRequired[
        "capo_textract.types.undetected_document_type_list.UndetectedDocumentTypeList"
    ]
    """<p>UndetectedDocumentTypes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingSummary) -> dict:
    out: dict = {}
    if "document_groups" in value:
        import capo_textract.types.document_group_list

        out["DocumentGroups"] = (
            capo_textract.types.document_group_list.serialize_aws_json_1_1(
                value["document_groups"]
            )
        )
    if "undetected_document_types" in value:
        import capo_textract.types.undetected_document_type_list

        out["UndetectedDocumentTypes"] = (
            capo_textract.types.undetected_document_type_list.serialize_aws_json_1_1(
                value["undetected_document_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingSummary:
    out: LendingSummary = {}  # type: ignore[typeddict-item]
    if data.get("DocumentGroups") is not None:
        import capo_textract.types.document_group_list

        out["document_groups"] = (
            capo_textract.types.document_group_list.deserialize_aws_json_1_1(
                data["DocumentGroups"]
            )
        )
    if data.get("UndetectedDocumentTypes") is not None:
        import capo_textract.types.undetected_document_type_list

        out["undetected_document_types"] = (
            capo_textract.types.undetected_document_type_list.deserialize_aws_json_1_1(
                data["UndetectedDocumentTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingSummary) -> dict:
    out: dict = {}
    if "document_groups" in value:
        import capo_textract.types.document_group_list

        out["DocumentGroups"] = capo_textract.types.document_group_list.serialize_cbor(
            value["document_groups"]
        )
    if "undetected_document_types" in value:
        import capo_textract.types.undetected_document_type_list

        out["UndetectedDocumentTypes"] = (
            capo_textract.types.undetected_document_type_list.serialize_cbor(
                value["undetected_document_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LendingSummary:
    out: LendingSummary = {}  # type: ignore[typeddict-item]
    if data.get("DocumentGroups") is not None:
        import capo_textract.types.document_group_list

        out["document_groups"] = (
            capo_textract.types.document_group_list.deserialize_cbor(
                data["DocumentGroups"]
            )
        )
    if data.get("UndetectedDocumentTypes") is not None:
        import capo_textract.types.undetected_document_type_list

        out["undetected_document_types"] = (
            capo_textract.types.undetected_document_type_list.deserialize_cbor(
                data["UndetectedDocumentTypes"]
            )
        )
    return out
