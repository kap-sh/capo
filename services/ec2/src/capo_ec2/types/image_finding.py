"""Generated from Smithy shape ``com.amazonaws.ec2#ImageFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.double
    import capo_ec2.types.image_finding_path_set
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.severity_label
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.string


class ImageFinding(TypedDict, closed=True):
    fix_available: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether a fix is available for the finding. This value is <code>true</code> when Amazon Inspector reports a full or partial fix for the finding.</p>"""
    score: NotRequired["capo_ec2.types.double.Double"]
    """<p>The Amazon Inspector score for the finding.</p>"""
    first_observed_at: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), when Amazon Inspector first observed the finding.</p>"""
    updated_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), when Amazon Inspector last updated the finding.</p>"""
    title: NotRequired["capo_ec2.types.string.String"]
    """<p>The title of the finding.</p>"""
    paths: NotRequired["capo_ec2.types.image_finding_path_set.ImageFindingPathSet"]
    """<p>The file paths in the AMI that are affected by the finding. Amazon EC2 returns up to 10 file paths for each finding.</p>"""
    severity_label: NotRequired["capo_ec2.types.severity_label.SeverityLabel"]
    """<p>The severity of the finding.</p> <p>The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:</p> <ul> <li> <p> <code>informational</code> - CVSS score of 0.</p> </li> <li> <p> <code>low</code> - CVSS score of 0.1 to 3.9.</p> </li> <li> <p> <code>medium</code> - CVSS score of 4.0 to 6.9.</p> </li> <li> <p> <code>high</code> - CVSS score of 7.0 to 8.9.</p> </li> <li> <p> <code>critical</code> - CVSS score of 9.0 to 10.0.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score">Software package vulnerability severity</a> in the <i>Amazon Inspector User Guide</i>.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the Amazon EBS snapshot of the AMI in which the finding was detected.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageFinding, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fix_available" in value:
        pairs.append(
            (f"{key_prefix}FixAvailable", "true" if value["fix_available"] else "false")
        )
    if "score" in value:
        pairs.append(
            (
                f"{key_prefix}Score",
                (
                    "NaN"
                    if value["score"] != value["score"]
                    else "Infinity"
                    if value["score"] == float("inf")
                    else "-Infinity"
                    if value["score"] == float("-inf")
                    else str(value["score"])
                ),
            )
        )
    if "first_observed_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["first_observed_at"], pairs, f"{key_prefix}FirstObservedAt"
        )
    if "updated_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )
    if "title" in value:
        pairs.append((f"{key_prefix}Title", str(value["title"])))
    if "paths" in value:
        import capo_ec2.types.image_finding_path_set

        capo_ec2.types.image_finding_path_set.serialize_ec2_query(
            value["paths"], pairs, f"{key_prefix}PathSet"
        )
    if "severity_label" in value:
        import capo_ec2.types.severity_label

        capo_ec2.types.severity_label.serialize_ec2_query(
            value["severity_label"], pairs, f"{key_prefix}SeverityLabel"
        )
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))


def deserialize_ec2_query(el: Element) -> ImageFinding:
    out: ImageFinding = {}  # type: ignore[typeddict-item]
    child_fix_available = el.find("fixAvailable")
    if child_fix_available is not None:
        out["fix_available"] = (child_fix_available.text or "").lower() == "true"
    child_score = el.find("score")
    if child_score is not None:
        out["score"] = float(child_score.text or "")
    child_first_observed_at = el.find("firstObservedAt")
    if child_first_observed_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["first_observed_at"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_first_observed_at
            )
        )
    child_updated_at = el.find("updatedAt")
    if child_updated_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["updated_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_updated_at
        )
    child_title = el.find("title")
    if child_title is not None:
        out["title"] = str(child_title.text or "")
    child_paths = el.find("pathSet")
    if child_paths is not None:
        import capo_ec2.types.image_finding_path_set

        out["paths"] = capo_ec2.types.image_finding_path_set.deserialize_ec2_query(
            child_paths
        )
    child_severity_label = el.find("severityLabel")
    if child_severity_label is not None:
        import capo_ec2.types.severity_label

        out["severity_label"] = capo_ec2.types.severity_label.deserialize_ec2_query(
            child_severity_label
        )
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    return out
