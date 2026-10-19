"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#IngestedFilesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer
    import capo_lookoutequipment.types.list_of_discarded_files


class IngestedFilesSummary(TypedDict, closed=True):
    total_number_of_files: "capo_lookoutequipment.types.integer.Integer"
    """<p>Indicates the total number of files that were submitted for ingestion.</p>"""
    ingested_number_of_files: "capo_lookoutequipment.types.integer.Integer"
    """<p>Indicates the number of files that were successfully ingested.</p>"""
    discarded_files: NotRequired[
        "capo_lookoutequipment.types.list_of_discarded_files.ListOfDiscardedFiles"
    ]
    """<p>Indicates the number of files that were discarded. A file could be discarded because its format is invalid (for example, a jpg or pdf) or not readable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestedFilesSummary) -> dict:
    out: dict = {}
    out["TotalNumberOfFiles"] = value["total_number_of_files"]
    out["IngestedNumberOfFiles"] = value["ingested_number_of_files"]
    if "discarded_files" in value:
        import capo_lookoutequipment.types.list_of_discarded_files

        out["DiscardedFiles"] = (
            capo_lookoutequipment.types.list_of_discarded_files.serialize_aws_json_1_0(
                value["discarded_files"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestedFilesSummary:
    out: IngestedFilesSummary = {}  # type: ignore[typeddict-item]
    if data.get("TotalNumberOfFiles") is not None:
        out["total_number_of_files"] = data["TotalNumberOfFiles"]
    else:
        out["total_number_of_files"] = 0
    if data.get("IngestedNumberOfFiles") is not None:
        out["ingested_number_of_files"] = data["IngestedNumberOfFiles"]
    else:
        out["ingested_number_of_files"] = 0
    if data.get("DiscardedFiles") is not None:
        import capo_lookoutequipment.types.list_of_discarded_files

        out["discarded_files"] = (
            capo_lookoutequipment.types.list_of_discarded_files.deserialize_aws_json_1_0(
                data["DiscardedFiles"]
            )
        )
    return out
