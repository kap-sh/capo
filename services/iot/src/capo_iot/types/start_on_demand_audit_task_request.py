"""Generated from Smithy shape ``com.amazonaws.iot#StartOnDemandAuditTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.target_audit_check_names


class StartOnDemandAuditTaskRequest(TypedDict, closed=True):
    target_check_names: "capo_iot.types.target_audit_check_names.TargetAuditCheckNames"
    """<p>Which checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are enabled or <code>UpdateAccountAuditConfiguration</code> to select which checks are enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOnDemandAuditTaskRequest) -> dict:
    out: dict = {}
    import capo_iot.types.target_audit_check_names

    out["targetCheckNames"] = capo_iot.types.target_audit_check_names.serialize_json(
        value["target_check_names"]
    )
    return out


def deserialize_json(data: dict) -> StartOnDemandAuditTaskRequest:
    out: StartOnDemandAuditTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetCheckNames") is not None:
        import capo_iot.types.target_audit_check_names

        out["target_check_names"] = (
            capo_iot.types.target_audit_check_names.deserialize_json(
                data["targetCheckNames"]
            )
        )
    else:
        out["target_check_names"] = []
    return out
