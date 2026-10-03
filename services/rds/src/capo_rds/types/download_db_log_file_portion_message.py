"""Generated from Smithy shape ``com.amazonaws.rds#DownloadDBLogFilePortionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer
    import capo_rds.types.string


class DownloadDBLogFilePortionMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The customer-assigned name of the DB instance that contains the log files you want to list.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    log_file_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the log file to be downloaded.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>The pagination token provided in the previous request or "0". If the Marker parameter is specified the response includes only records beyond the marker until the end of the file or up to NumberOfLines.</p>"""
    number_of_lines: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The number of lines to download. If the number of lines specified results in a file over 1 MB in size, the file is truncated at 1 MB in size.</p> <p>If the NumberOfLines parameter is specified, then the block of lines returned can be from the beginning or the end of the log file, depending on the value of the Marker parameter.</p> <ul> <li> <p>If neither Marker or NumberOfLines are specified, the entire log file is returned up to a maximum of 10000 lines, starting with the most recent log entries first.</p> </li> <li> <p>If NumberOfLines is specified and Marker isn't specified, then the most recent lines from the end of the log file are returned.</p> </li> <li> <p>If Marker is specified as "0", then the specified number of lines from the beginning of the log file are returned.</p> </li> <li> <p>You can download the log file in blocks of lines by specifying the size of the block using the NumberOfLines parameter, and by specifying a value of "0" for the Marker parameter in your first request. Include the Marker value returned in the response as the Marker value for the next request, continuing until the AdditionalDataPending response element returns false.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DownloadDBLogFilePortionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "log_file_name" in value:
        pairs.append((f"{key_prefix}LogFileName", str(value["log_file_name"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "number_of_lines" in value:
        pairs.append((f"{key_prefix}NumberOfLines", str(value["number_of_lines"])))


def deserialize_query(el: Element) -> DownloadDBLogFilePortionMessage:
    out: DownloadDBLogFilePortionMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_log_file_name = el.find("LogFileName")
    if child_log_file_name is not None:
        out["log_file_name"] = str(child_log_file_name.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_number_of_lines = el.find("NumberOfLines")
    if child_number_of_lines is not None:
        out["number_of_lines"] = int(child_number_of_lines.text or "")
    return out
