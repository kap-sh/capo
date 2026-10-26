"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CreateScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.resource_id
    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.scan_name_arn
    import capo_codeguru_security.types.scan_state
    import capo_codeguru_security.types.uuid


class CreateScanResponse(TypedDict, closed=True):
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan.</p>"""
    run_id: "capo_codeguru_security.types.uuid.Uuid"
    """<p>UUID that identifies the individual scan run.</p>"""
    resource_id: "capo_codeguru_security.types.resource_id.ResourceId"
    """<p>The identifier for the resource object that contains resources that were scanned.</p>"""
    scan_state: "capo_codeguru_security.types.scan_state.ScanState"
    """<p>The current state of the scan. Returns either <code>InProgress</code>, <code>Successful</code>, or <code>Failed</code>.</p>"""
    scan_name_arn: NotRequired["capo_codeguru_security.types.scan_name_arn.ScanNameArn"]
    """<p>The ARN for the scan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScanResponse) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["runId"] = value["run_id"]
    import capo_codeguru_security.types.resource_id

    out["resourceId"] = capo_codeguru_security.types.resource_id.serialize_json(
        value["resource_id"]
    )
    import capo_codeguru_security.types.scan_state

    out["scanState"] = capo_codeguru_security.types.scan_state.serialize_json(
        value["scan_state"]
    )
    if "scan_name_arn" in value:
        out["scanNameArn"] = value["scan_name_arn"]
    return out


def deserialize_json(data: dict) -> CreateScanResponse:
    out: CreateScanResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    else:
        out["run_id"] = ""
    if data.get("resourceId") is not None:
        import capo_codeguru_security.types.resource_id

        out["resource_id"] = capo_codeguru_security.types.resource_id.deserialize_json(
            data["resourceId"]
        )
    else:
        out["resource_id"] = {"$unknown": {"name": ""}}
    if data.get("scanState") is not None:
        import capo_codeguru_security.types.scan_state

        out["scan_state"] = capo_codeguru_security.types.scan_state.deserialize_json(
            data["scanState"]
        )
    else:
        import typing

        out["scan_state"] = typing.cast(
            "capo_codeguru_security.types.scan_state.ScanState", ""
        )
    if data.get("scanNameArn") is not None:
        out["scan_name_arn"] = data["scanNameArn"]
    return out
