"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#BatchGetFindingsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.error_code
    import capo_codeguru_security.types.scan_name


class BatchGetFindingsError(TypedDict, closed=True):
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan that generated the finding.</p>"""
    finding_id: "str"
    """<p>The finding ID of the finding that was not fetched.</p>"""
    error_code: "capo_codeguru_security.types.error_code.ErrorCode"
    """<p>A code associated with the type of error.</p>"""
    message: "str"
    """<p>Describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsError) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["findingId"] = value["finding_id"]
    import capo_codeguru_security.types.error_code

    out["errorCode"] = capo_codeguru_security.types.error_code.serialize_json(
        value["error_code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetFindingsError:
    out: BatchGetFindingsError = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("errorCode") is not None:
        import capo_codeguru_security.types.error_code

        out["error_code"] = capo_codeguru_security.types.error_code.deserialize_json(
            data["errorCode"]
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_codeguru_security.types.error_code.ErrorCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
