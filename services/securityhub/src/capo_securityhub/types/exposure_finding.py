"""Generated from Smithy shape ``com.amazonaws.securityhub#ExposureFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.exposure_impact
    import capo_securityhub.types.exposure_severity
    import capo_securityhub.types.non_empty_string


class ExposureFinding(TypedDict, closed=True):
    metadata_uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier (ID) of the Security Hub exposure finding, found under the <code>metadata.uid</code> field of the finding.</p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The title of the exposure finding.</p>"""
    previous_severity: NotRequired[
        "capo_securityhub.types.exposure_severity.ExposureSeverity"
    ]
    """<p>The severity of the exposure finding before the remediation target is resolved.</p>"""
    projected_severity: NotRequired[
        "capo_securityhub.types.exposure_severity.ExposureSeverity"
    ]
    """<p>The severity of the exposure finding after the remediation target is resolved.</p>"""
    impact: NotRequired["capo_securityhub.types.exposure_impact.ExposureImpact"]
    """<p>The impact resolving a remediation target has on the exposure finding.</p> <ul> <li> <p> <code>Reduces</code> specifies that resolving the remediation target lowers the severity of the exposure finding, but does not resolve it.</p> </li> <li> <p> <code>Resolves</code> specifies that resolving the remediation target resolves the exposure finding.</p> </li> <li> <p> <code>Unchanged</code> specifies that resolving the remediation target does not change the severity of the exposure finding.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExposureFinding) -> dict:
    out: dict = {}
    if "metadata_uid" in value:
        out["MetadataUid"] = value["metadata_uid"]
    if "title" in value:
        out["Title"] = value["title"]
    if "previous_severity" in value:
        import capo_securityhub.types.exposure_severity

        out["PreviousSeverity"] = (
            capo_securityhub.types.exposure_severity.serialize_json(
                value["previous_severity"]
            )
        )
    if "projected_severity" in value:
        import capo_securityhub.types.exposure_severity

        out["ProjectedSeverity"] = (
            capo_securityhub.types.exposure_severity.serialize_json(
                value["projected_severity"]
            )
        )
    if "impact" in value:
        import capo_securityhub.types.exposure_impact

        out["Impact"] = capo_securityhub.types.exposure_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> ExposureFinding:
    out: ExposureFinding = {}  # type: ignore[typeddict-item]
    if data.get("MetadataUid") is not None:
        out["metadata_uid"] = data["MetadataUid"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("PreviousSeverity") is not None:
        import capo_securityhub.types.exposure_severity

        out["previous_severity"] = (
            capo_securityhub.types.exposure_severity.deserialize_json(
                data["PreviousSeverity"]
            )
        )
    if data.get("ProjectedSeverity") is not None:
        import capo_securityhub.types.exposure_severity

        out["projected_severity"] = (
            capo_securityhub.types.exposure_severity.deserialize_json(
                data["ProjectedSeverity"]
            )
        )
    if data.get("Impact") is not None:
        import capo_securityhub.types.exposure_impact

        out["impact"] = capo_securityhub.types.exposure_impact.deserialize_json(
            data["Impact"]
        )
    return out
