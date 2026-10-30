"""Generated from Smithy shape ``com.amazonaws.ec2#ScanResultCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.max_days_since_fix_available_value
    import capo_ec2.types.max_days_since_last_finding_scan_value
    import capo_ec2.types.severity_label


class ScanResultCondition(TypedDict, closed=True):
    max_days_since_last_finding_scan: NotRequired[
        "capo_ec2.types.max_days_since_last_finding_scan_value.MaxDaysSinceLastFindingScanValue"
    ]
    """<p>The maximum number of days that have elapsed since Amazon Inspector last scanned the AMI. For example, a value of <code>7</code> allows AMIs that were scanned within the last 7 days. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    maximum_severity_label: NotRequired["capo_ec2.types.severity_label.SeverityLabel"]
    """<p>The maximum severity that an AMI's Amazon Inspector findings can have for the AMI to be allowed. Findings count whether or not a fix is available. For example, a value of <code>medium</code> allows AMIs whose highest severity is <code>informational</code>, <code>low</code>, or <code>medium</code>.</p> <p>The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:</p> <ul> <li> <p> <code>informational</code> - CVSS score of 0.</p> </li> <li> <p> <code>low</code> - CVSS score of 0.1 to 3.9.</p> </li> <li> <p> <code>medium</code> - CVSS score of 4.0 to 6.9.</p> </li> <li> <p> <code>high</code> - CVSS score of 7.0 to 8.9.</p> </li> <li> <p> <code>critical</code> - CVSS score of 9.0 to 10.0.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score">Software package vulnerability severity</a> in the <i>Amazon Inspector User Guide</i>.</p> <p>A scanned AMI that has no findings meets this limit.</p> <p>AMIs that Amazon Inspector has not scanned are not allowed when you specify this condition.</p>"""
    max_days_since_informational_fix_available: NotRequired[
        "capo_ec2.types.max_days_since_fix_available_value.MaxDaysSinceFixAvailableValue"
    ]
    """<p>The maximum number of days since Amazon Inspector reported a fix as available for an <code>informational</code> severity finding on the AMI. For example, a value of <code>7</code> does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.</p> <p>A scanned AMI that has no <code>informational</code> severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    max_days_since_low_fix_available: NotRequired[
        "capo_ec2.types.max_days_since_fix_available_value.MaxDaysSinceFixAvailableValue"
    ]
    """<p>The maximum number of days since Amazon Inspector reported a fix as available for a <code>low</code> severity finding on the AMI. For example, a value of <code>7</code> does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.</p> <p>A scanned AMI that has no <code>low</code> severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    max_days_since_medium_fix_available: NotRequired[
        "capo_ec2.types.max_days_since_fix_available_value.MaxDaysSinceFixAvailableValue"
    ]
    """<p>The maximum number of days since Amazon Inspector reported a fix as available for a <code>medium</code> severity finding on the AMI. For example, a value of <code>7</code> does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.</p> <p>A scanned AMI that has no <code>medium</code> severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    max_days_since_high_fix_available: NotRequired[
        "capo_ec2.types.max_days_since_fix_available_value.MaxDaysSinceFixAvailableValue"
    ]
    """<p>The maximum number of days since Amazon Inspector reported a fix as available for a <code>high</code> severity finding on the AMI. For example, a value of <code>7</code> does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.</p> <p>A scanned AMI that has no <code>high</code> severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    max_days_since_critical_fix_available: NotRequired[
        "capo_ec2.types.max_days_since_fix_available_value.MaxDaysSinceFixAvailableValue"
    ]
    """<p>The maximum number of days since Amazon Inspector reported a fix as available for a <code>critical</code> severity finding on the AMI. For example, a value of <code>7</code> does not allow an AMI if Amazon Inspector reported such a fix more than 7 days ago.</p> <p>A scanned AMI that has no <code>critical</code> severity finding with a fix available meets this limit. AMIs that Amazon Inspector has not scanned are not allowed.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScanResultCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "max_days_since_last_finding_scan" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceLastFindingScan",
                str(value["max_days_since_last_finding_scan"]),
            )
        )
    if "maximum_severity_label" in value:
        import capo_ec2.types.severity_label

        capo_ec2.types.severity_label.serialize_ec2_query(
            value["maximum_severity_label"], pairs, f"{key_prefix}MaximumSeverityLabel"
        )
    if "max_days_since_informational_fix_available" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceInformationalFixAvailable",
                str(value["max_days_since_informational_fix_available"]),
            )
        )
    if "max_days_since_low_fix_available" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceLowFixAvailable",
                str(value["max_days_since_low_fix_available"]),
            )
        )
    if "max_days_since_medium_fix_available" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceMediumFixAvailable",
                str(value["max_days_since_medium_fix_available"]),
            )
        )
    if "max_days_since_high_fix_available" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceHighFixAvailable",
                str(value["max_days_since_high_fix_available"]),
            )
        )
    if "max_days_since_critical_fix_available" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDaysSinceCriticalFixAvailable",
                str(value["max_days_since_critical_fix_available"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ScanResultCondition:
    out: ScanResultCondition = {}  # type: ignore[typeddict-item]
    child_max_days_since_last_finding_scan = el.find("maxDaysSinceLastFindingScan")
    if child_max_days_since_last_finding_scan is not None:
        out["max_days_since_last_finding_scan"] = int(
            child_max_days_since_last_finding_scan.text or ""
        )
    child_maximum_severity_label = el.find("maximumSeverityLabel")
    if child_maximum_severity_label is not None:
        import capo_ec2.types.severity_label

        out["maximum_severity_label"] = (
            capo_ec2.types.severity_label.deserialize_ec2_query(
                child_maximum_severity_label
            )
        )
    child_max_days_since_informational_fix_available = el.find(
        "maxDaysSinceInformationalFixAvailable"
    )
    if child_max_days_since_informational_fix_available is not None:
        out["max_days_since_informational_fix_available"] = int(
            child_max_days_since_informational_fix_available.text or ""
        )
    child_max_days_since_low_fix_available = el.find("maxDaysSinceLowFixAvailable")
    if child_max_days_since_low_fix_available is not None:
        out["max_days_since_low_fix_available"] = int(
            child_max_days_since_low_fix_available.text or ""
        )
    child_max_days_since_medium_fix_available = el.find(
        "maxDaysSinceMediumFixAvailable"
    )
    if child_max_days_since_medium_fix_available is not None:
        out["max_days_since_medium_fix_available"] = int(
            child_max_days_since_medium_fix_available.text or ""
        )
    child_max_days_since_high_fix_available = el.find("maxDaysSinceHighFixAvailable")
    if child_max_days_since_high_fix_available is not None:
        out["max_days_since_high_fix_available"] = int(
            child_max_days_since_high_fix_available.text or ""
        )
    child_max_days_since_critical_fix_available = el.find(
        "maxDaysSinceCriticalFixAvailable"
    )
    if child_max_days_since_critical_fix_available is not None:
        out["max_days_since_critical_fix_available"] = int(
            child_max_days_since_critical_fix_available.text or ""
        )
    return out
