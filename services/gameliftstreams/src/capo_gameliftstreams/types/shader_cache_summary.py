"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ShaderCacheSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.arn_list
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.shader_cache_status


class ShaderCacheSummary(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>A unique identifier for the shader cache, formatted as a 32-character hexadecimal string. Format is <code>1271e693c50b940e228582f1ccdd4e27</code>.</p>"""
    application_arn: "capo_gameliftstreams.types.arn.Arn"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""
    status: NotRequired[
        "capo_gameliftstreams.types.shader_cache_status.ShaderCacheStatus"
    ]
    """<p>The current status of the shader cache. Possible statuses include the following:</p> <ul> <li> <p> <code>INITIALIZED</code>: Amazon GameLift Streams received the request and is preparing the shader cache.</p> </li> <li> <p> <code>PROCESSING</code>: Amazon GameLift Streams is replicating the shader cache to the streaming locations in the associated stream groups.</p> </li> <li> <p> <code>READY</code>: The shader cache is replicated and available for use in stream sessions.</p> </li> <li> <p> <code>DELETING</code>: Amazon GameLift Streams is deleting the shader cache.</p> </li> <li> <p> <code>ERROR</code>: An error occurred during shader cache processing. Create a new shader cache to try again.</p> </li> </ul>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    storage_bytes: NotRequired["int"]
    """<p>The total storage used by all compiled shader files in this shader cache, in bytes.</p>"""
    associated_stream_groups: NotRequired["capo_gameliftstreams.types.arn_list.ArnList"]
    """<p>The stream groups compatible with this shader cache. Compatibility is based on GPU type and GPU driver version. For more information on shader cache compatibility, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/shader-caches.html">Shader caches</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> <p>This value is a set of <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> that uniquely identify stream group resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShaderCacheSummary) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    out["ApplicationArn"] = value["application_arn"]
    if "status" in value:
        import capo_gameliftstreams.types.shader_cache_status

        out["Status"] = capo_gameliftstreams.types.shader_cache_status.serialize_json(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            capo_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "storage_bytes" in value:
        out["StorageBytes"] = value["storage_bytes"]
    if "associated_stream_groups" in value:
        import capo_gameliftstreams.types.arn_list

        out["AssociatedStreamGroups"] = (
            capo_gameliftstreams.types.arn_list.serialize_json(
                value["associated_stream_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ShaderCacheSummary:
    out: ShaderCacheSummary = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("ShaderCacheSummary.identifier required")
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError("ShaderCacheSummary.application_arn required")
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.shader_cache_status

        out["status"] = capo_gameliftstreams.types.shader_cache_status.deserialize_json(
            data["Status"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("StorageBytes") is not None:
        out["storage_bytes"] = data["StorageBytes"]
    if data.get("AssociatedStreamGroups") is not None:
        import capo_gameliftstreams.types.arn_list

        out["associated_stream_groups"] = (
            capo_gameliftstreams.types.arn_list.deserialize_json(
                data["AssociatedStreamGroups"]
            )
        )
    return out
