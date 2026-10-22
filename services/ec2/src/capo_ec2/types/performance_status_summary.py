"""Generated from Smithy shape ``com.amazonaws.ec2#PerformanceStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.summary_status


class PerformanceStatusSummary(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.summary_status.SummaryStatus"]
    """<p>The current status.</p>"""
    impaired_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the performance status became impaired.</p>"""
    remediation: NotRequired["capo_ec2.types.string.String"]
    """<p>The recommended action to remediate the impaired instance, if one is available. This value is returned only when the instance is impaired.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PerformanceStatusSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ec2.types.summary_status

        capo_ec2.types.summary_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "impaired_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["impaired_since"], pairs, f"{key_prefix}ImpairedSince"
        )
    if "remediation" in value:
        pairs.append((f"{key_prefix}Remediation", str(value["remediation"])))


def deserialize_ec2_query(el: Element) -> PerformanceStatusSummary:
    out: PerformanceStatusSummary = {}  # type: ignore[typeddict-item]
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.summary_status

        out["status"] = capo_ec2.types.summary_status.deserialize_ec2_query(
            child_status
        )
    child_impaired_since = el.find("impairedSince")
    if child_impaired_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["impaired_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_impaired_since
            )
        )
    child_remediation = el.find("remediation")
    if child_remediation is not None:
        out["remediation"] = str(child_remediation.text or "")
    return out
