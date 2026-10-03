"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_source_status_list
    import capo_securitylake.types.ocsf_event_class_list


class DataLakeSource(TypedDict, closed=True):
    account: NotRequired["str"]
    """<p>The ID of the Security Lake account for which logs are collected.</p>"""
    source_name: NotRequired["str"]
    """<p>The supported Amazon Web Services services from which logs and events are collected. Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>"""
    event_classes: NotRequired[
        "capo_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
    ]
    """<p>The Open Cybersecurity Schema Framework (OCSF) event classes describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass.html">Supported OCSF Event classes</a> in the Amazon Security Lake User Guide.</p>"""
    source_statuses: NotRequired[
        "capo_securitylake.types.data_lake_source_status_list.DataLakeSourceStatusList"
    ]
    """<p>The log status for the Security Lake account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSource) -> dict:
    out: dict = {}
    if "account" in value:
        out["account"] = value["account"]
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "event_classes" in value:
        import capo_securitylake.types.ocsf_event_class_list

        out["eventClasses"] = (
            capo_securitylake.types.ocsf_event_class_list.serialize_json(
                value["event_classes"]
            )
        )
    if "source_statuses" in value:
        import capo_securitylake.types.data_lake_source_status_list

        out["sourceStatuses"] = (
            capo_securitylake.types.data_lake_source_status_list.serialize_json(
                value["source_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeSource:
    out: DataLakeSource = {}  # type: ignore[typeddict-item]
    if data.get("account") is not None:
        out["account"] = data["account"]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    if data.get("eventClasses") is not None:
        import capo_securitylake.types.ocsf_event_class_list

        out["event_classes"] = (
            capo_securitylake.types.ocsf_event_class_list.deserialize_json(
                data["eventClasses"]
            )
        )
    if data.get("sourceStatuses") is not None:
        import capo_securitylake.types.data_lake_source_status_list

        out["source_statuses"] = (
            capo_securitylake.types.data_lake_source_status_list.deserialize_json(
                data["sourceStatuses"]
            )
        )
    return out
