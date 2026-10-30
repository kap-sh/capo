"""Generated from Smithy shape ``com.amazonaws.ec2#ScanResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.severity_label


class ScanResults(TypedDict, closed=True):
    highest_finding_severity_label: NotRequired[
        "capo_ec2.types.severity_label.SeverityLabel"
    ]
    """<p>The highest severity among the AMI's Amazon Inspector findings, whether or not a fix is available.</p> <p>The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:</p> <ul> <li> <p> <code>informational</code> - CVSS score of 0.</p> </li> <li> <p> <code>low</code> - CVSS score of 0.1 to 3.9.</p> </li> <li> <p> <code>medium</code> - CVSS score of 4.0 to 6.9.</p> </li> <li> <p> <code>high</code> - CVSS score of 7.0 to 8.9.</p> </li> <li> <p> <code>critical</code> - CVSS score of 9.0 to 10.0.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score">Software package vulnerability severity</a> in the <i>Amazon Inspector User Guide</i>.</p> <p>This value is present only if the AMI has at least one finding.</p>"""
    finding_scan_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), of the most recent Amazon Inspector scan of the AMI.</p>"""
    informational_fix_available_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for an <code>informational</code> severity finding on the AMI. This value is present only if the AMI has at least one <code>informational</code> severity finding with a fix available. Amazon Inspector recomputes this value on each scan.</p>"""
    low_fix_available_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a <code>low</code> severity finding on the AMI. This value is present only if the AMI has at least one <code>low</code> severity finding with a fix available. Amazon Inspector recomputes this value on each scan.</p>"""
    medium_fix_available_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a <code>medium</code> severity finding on the AMI. This value is present only if the AMI has at least one <code>medium</code> severity finding with a fix available. Amazon Inspector recomputes this value on each scan.</p>"""
    high_fix_available_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a <code>high</code> severity finding on the AMI. This value is present only if the AMI has at least one <code>high</code> severity finding with a fix available. Amazon Inspector recomputes this value on each scan.</p>"""
    critical_fix_available_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a <code>critical</code> severity finding on the AMI. This value is present only if the AMI has at least one <code>critical</code> severity finding with a fix available. Amazon Inspector recomputes this value on each scan.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScanResults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "highest_finding_severity_label" in value:
        import capo_ec2.types.severity_label

        capo_ec2.types.severity_label.serialize_ec2_query(
            value["highest_finding_severity_label"],
            pairs,
            f"{key_prefix}HighestFindingSeverityLabel",
        )
    if "finding_scan_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["finding_scan_date"], pairs, f"{key_prefix}FindingScanDate"
        )
    if "informational_fix_available_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["informational_fix_available_since"],
            pairs,
            f"{key_prefix}InformationalFixAvailableSince",
        )
    if "low_fix_available_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["low_fix_available_since"], pairs, f"{key_prefix}LowFixAvailableSince"
        )
    if "medium_fix_available_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["medium_fix_available_since"],
            pairs,
            f"{key_prefix}MediumFixAvailableSince",
        )
    if "high_fix_available_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["high_fix_available_since"],
            pairs,
            f"{key_prefix}HighFixAvailableSince",
        )
    if "critical_fix_available_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["critical_fix_available_since"],
            pairs,
            f"{key_prefix}CriticalFixAvailableSince",
        )


def deserialize_ec2_query(el: Element) -> ScanResults:
    out: ScanResults = {}  # type: ignore[typeddict-item]
    child_highest_finding_severity_label = el.find("highestFindingSeverityLabel")
    if child_highest_finding_severity_label is not None:
        import capo_ec2.types.severity_label

        out["highest_finding_severity_label"] = (
            capo_ec2.types.severity_label.deserialize_ec2_query(
                child_highest_finding_severity_label
            )
        )
    child_finding_scan_date = el.find("findingScanDate")
    if child_finding_scan_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["finding_scan_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_finding_scan_date
            )
        )
    child_informational_fix_available_since = el.find("informationalFixAvailableSince")
    if child_informational_fix_available_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["informational_fix_available_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_informational_fix_available_since
            )
        )
    child_low_fix_available_since = el.find("lowFixAvailableSince")
    if child_low_fix_available_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["low_fix_available_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_low_fix_available_since
            )
        )
    child_medium_fix_available_since = el.find("mediumFixAvailableSince")
    if child_medium_fix_available_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["medium_fix_available_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_medium_fix_available_since
            )
        )
    child_high_fix_available_since = el.find("highFixAvailableSince")
    if child_high_fix_available_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["high_fix_available_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_high_fix_available_since
            )
        )
    child_critical_fix_available_since = el.find("criticalFixAvailableSince")
    if child_critical_fix_available_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["critical_fix_available_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_critical_fix_available_since
            )
        )
    return out
