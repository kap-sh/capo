"""Generated from Smithy shape ``com.amazonaws.guardduty#S3Activity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.activity_window
    import capo_guardduty.types.count
    import capo_guardduty.types.enrichment
    import capo_guardduty.types.investigation_actor
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class S3Activity(TypedDict, closed=True):
    api: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon S3 API operation that was called.</p>"""
    affected_bucket: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the affected bucket, or <code>account-wide</code> if the activity isn't limited to one bucket.</p>"""
    other_s3_activity: NotRequired["capo_guardduty.types.string.String"]
    """<p>Other Amazon S3 activity that is related to the observation.</p>"""
    non_s3_activity: NotRequired["capo_guardduty.types.string.String"]
    """<p>Related activity on Amazon Web Services services other than Amazon S3.</p>"""
    session_assessment: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of the session in which the activity occurred.</p>"""
    event_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of events.</p>"""
    actor: NotRequired["capo_guardduty.types.investigation_actor.InvestigationActor"]
    """<p>The identity that performed the activity.</p>"""
    source_ip: NotRequired["capo_guardduty.types.string.String"]
    """<p>The source address of the activity, or a description of the source.</p>"""
    enrichment: NotRequired["capo_guardduty.types.enrichment.Enrichment"]
    """<p>Additional context about the activity, such as geolocation information.</p>"""
    activity_window: NotRequired["capo_guardduty.types.activity_window.ActivityWindow"]
    """<p>The time range of the activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Activity) -> dict:
    out: dict = {}
    if "api" in value:
        out["api"] = value["api"]
    if "affected_bucket" in value:
        out["affectedBucket"] = value["affected_bucket"]
    if "other_s3_activity" in value:
        out["otherS3Activity"] = value["other_s3_activity"]
    if "non_s3_activity" in value:
        out["nonS3Activity"] = value["non_s3_activity"]
    if "session_assessment" in value:
        out["sessionAssessment"] = value["session_assessment"]
    if "event_count" in value:
        out["eventCount"] = value["event_count"]
    if "actor" in value:
        import capo_guardduty.types.investigation_actor

        out["actor"] = capo_guardduty.types.investigation_actor.serialize_json(
            value["actor"]
        )
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "enrichment" in value:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.serialize_json(
            value["enrichment"]
        )
    if "activity_window" in value:
        import capo_guardduty.types.activity_window

        out["activityWindow"] = capo_guardduty.types.activity_window.serialize_json(
            value["activity_window"]
        )
    return out


def deserialize_json(data: dict) -> S3Activity:
    out: S3Activity = {}  # type: ignore[typeddict-item]
    if data.get("api") is not None:
        out["api"] = data["api"]
    if data.get("affectedBucket") is not None:
        out["affected_bucket"] = data["affectedBucket"]
    if data.get("otherS3Activity") is not None:
        out["other_s3_activity"] = data["otherS3Activity"]
    if data.get("nonS3Activity") is not None:
        out["non_s3_activity"] = data["nonS3Activity"]
    if data.get("sessionAssessment") is not None:
        out["session_assessment"] = data["sessionAssessment"]
    if data.get("eventCount") is not None:
        out["event_count"] = data["eventCount"]
    if data.get("actor") is not None:
        import capo_guardduty.types.investigation_actor

        out["actor"] = capo_guardduty.types.investigation_actor.deserialize_json(
            data["actor"]
        )
    if data.get("sourceIp") is not None:
        out["source_ip"] = data["sourceIp"]
    if data.get("enrichment") is not None:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.deserialize_json(
            data["enrichment"]
        )
    if data.get("activityWindow") is not None:
        import capo_guardduty.types.activity_window

        out["activity_window"] = capo_guardduty.types.activity_window.deserialize_json(
            data["activityWindow"]
        )
    return out
