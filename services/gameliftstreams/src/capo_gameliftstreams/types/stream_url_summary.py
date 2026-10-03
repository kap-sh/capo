"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamUrlSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.id
    import capo_gameliftstreams.types.remaining_uses
    import capo_gameliftstreams.types.session_length_seconds
    import capo_gameliftstreams.types.stream_session_stream_url
    import capo_gameliftstreams.types.stream_url_status
    import capo_gameliftstreams.types.stream_url_status_reason
    import capo_gameliftstreams.types.usage_limit


class StreamUrlSummary(TypedDict, closed=True):
    arn: "capo_gameliftstreams.types.arn.Arn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the stream URL across all Amazon Web Services Regions. Format is <code>arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamurl/[stream group resource ID]/[stream URL resource ID]</code>.</p>"""
    stream_url_id: NotRequired["capo_gameliftstreams.types.id.Id"]
    """<p>The unique identifier for the stream URL resource, for example <code>su-1AB2C3De4</code>.</p>"""
    stream_url: NotRequired[
        "capo_gameliftstreams.types.stream_session_stream_url.StreamSessionStreamUrl"
    ]
    """<p>The shareable stream URL. Distribute this URL to end users so that they can start and play a stream session in a hosted web player. Treat the stream URL as a secret. Anyone who has it can start a stream session until the stream URL expires, is revoked, or reaches its usage limit.</p>"""
    status: NotRequired["capo_gameliftstreams.types.stream_url_status.StreamUrlStatus"]
    """<p>The current status of the stream URL. Possible statuses include the following:</p> <ul> <li> <p> <code>ACTIVE</code>: The stream URL is valid and can start stream sessions.</p> </li> <li> <p> <code>EXPIRED</code>: The stream URL has passed its expiration time and can no longer start stream sessions.</p> </li> <li> <p> <code>REVOKED</code>: The stream URL was revoked and can no longer start stream sessions.</p> </li> <li> <p> <code>LIMIT_REACHED</code>: The stream URL has been used the maximum number of times and can no longer start stream sessions.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_gameliftstreams.types.stream_url_status_reason.StreamUrlStatusReason"
    ]
    """<p>Additional information about why the stream URL is in its current status. Amazon GameLift Streams populates this value when the status is <code>REVOKED</code>. Possible values include the following:</p> <ul> <li> <p> <code>userRevoked</code>: You revoked the stream URL.</p> </li> <li> <p> <code>revokedAndTerminatingSessions</code>: You revoked the stream URL and Amazon GameLift Streams is ending its running stream sessions.</p> </li> <li> <p> <code>revokedAndSessionsTerminated</code>: You revoked the stream URL and its running stream sessions have ended.</p> </li> <li> <p> <code>streamGroupDeleted</code>: The stream group was deleted, which revoked the stream URL.</p> </li> <li> <p> <code>applicationDeleted</code>: The application was deleted, which revoked the stream URL.</p> </li> </ul>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the stream URL expires and stops accepting new stream sessions. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    usage_limit: NotRequired["capo_gameliftstreams.types.usage_limit.UsageLimit"]
    """<p>The maximum number of times the stream URL can start a stream session.</p>"""
    remaining_uses: NotRequired[
        "capo_gameliftstreams.types.remaining_uses.RemainingUses"
    ]
    """<p>The number of times the stream URL can still be used to start a stream session.</p>"""
    stream_group_arn: NotRequired["capo_gameliftstreams.types.arn.Arn"]
    """<p>The stream group that runs the stream sessions.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. </p>"""
    application_arn: NotRequired["capo_gameliftstreams.types.arn.Arn"]
    """<p>The application that runs in the stream sessions.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""
    session_length_seconds: NotRequired[
        "capo_gameliftstreams.types.session_length_seconds.SessionLengthSeconds"
    ]
    """<p>The maximum length of time, in seconds, that a stream session started from this stream URL can run.</p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>The descriptive label for the stream URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamUrlSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "stream_url_id" in value:
        out["StreamUrlId"] = value["stream_url_id"]
    if "stream_url" in value:
        out["StreamUrl"] = value["stream_url"]
    if "status" in value:
        import capo_gameliftstreams.types.stream_url_status

        out["Status"] = capo_gameliftstreams.types.stream_url_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_gameliftstreams.types.stream_url_status_reason

        out["StatusReason"] = (
            capo_gameliftstreams.types.stream_url_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "expires_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["ExpiresAt"] = capo_gameliftstreams.types._prelude.timestamp.serialize_json(
            value["expires_at"]
        )
    if "created_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["CreatedAt"] = capo_gameliftstreams.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "usage_limit" in value:
        out["UsageLimit"] = value["usage_limit"]
    if "remaining_uses" in value:
        out["RemainingUses"] = value["remaining_uses"]
    if "stream_group_arn" in value:
        out["StreamGroupArn"] = value["stream_group_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "session_length_seconds" in value:
        out["SessionLengthSeconds"] = value["session_length_seconds"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StreamUrlSummary:
    out: StreamUrlSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StreamUrlSummary.arn required")
    if data.get("StreamUrlId") is not None:
        out["stream_url_id"] = data["StreamUrlId"]
    if data.get("StreamUrl") is not None:
        out["stream_url"] = data["StreamUrl"]
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.stream_url_status

        out["status"] = capo_gameliftstreams.types.stream_url_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        import capo_gameliftstreams.types.stream_url_status_reason

        out["status_reason"] = (
            capo_gameliftstreams.types.stream_url_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("ExpiresAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["expires_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["ExpiresAt"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["created_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UsageLimit") is not None:
        out["usage_limit"] = data["UsageLimit"]
    if data.get("RemainingUses") is not None:
        out["remaining_uses"] = data["RemainingUses"]
    if data.get("StreamGroupArn") is not None:
        out["stream_group_arn"] = data["StreamGroupArn"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("SessionLengthSeconds") is not None:
        out["session_length_seconds"] = data["SessionLengthSeconds"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
