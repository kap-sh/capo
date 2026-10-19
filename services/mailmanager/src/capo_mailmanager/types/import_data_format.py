"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportDataFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.import_data_type


class ImportDataFormat(TypedDict, closed=True):
    import_data_type: "capo_mailmanager.types.import_data_type.ImportDataType"
    """<p>The type of file that would be passed as an input for the address list import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDataFormat) -> dict:
    out: dict = {}
    import capo_mailmanager.types.import_data_type

    out["ImportDataType"] = (
        capo_mailmanager.types.import_data_type.serialize_aws_json_1_0(
            value["import_data_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDataFormat:
    out: ImportDataFormat = {}  # type: ignore[typeddict-item]
    if data.get("ImportDataType") is not None:
        import capo_mailmanager.types.import_data_type

        out["import_data_type"] = (
            capo_mailmanager.types.import_data_type.deserialize_aws_json_1_0(
                data["ImportDataType"]
            )
        )
    else:
        import typing

        out["import_data_type"] = typing.cast(
            "capo_mailmanager.types.import_data_type.ImportDataType", ""
        )
    return out
