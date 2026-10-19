"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEphemerisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.customer_ephemeris_priority
    import capo_groundstation.types.ephemeris_data
    import capo_groundstation.types.key_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.uuid


class CreateEphemerisRequest(TypedDict, closed=True):
    satellite_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.</p>"""
    enabled: NotRequired["bool"]
    """<p>Set to <code>true</code> to enable the ephemeris after validation. Set to <code>false</code> to keep it disabled.</p>"""
    priority: NotRequired[
        "capo_groundstation.types.customer_ephemeris_priority.CustomerEphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>An overall expiration time for the ephemeris in UTC, after which it will become <code>EXPIRED</code>.</p>"""
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>A name that you can use to identify the ephemeris.</p>"""
    kms_key_arn: NotRequired["capo_groundstation.types.key_arn.KeyArn"]
    """<p>The ARN of the KMS key to use for encrypting the ephemeris.</p>"""
    ephemeris: NotRequired["capo_groundstation.types.ephemeris_data.EphemerisData"]
    """<p>Ephemeris data.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to an ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEphemerisRequest) -> dict:
    out: dict = {}
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "expiration_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["expirationTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    out["name"] = value["name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "ephemeris" in value:
        import capo_groundstation.types.ephemeris_data

        out["ephemeris"] = capo_groundstation.types.ephemeris_data.serialize_json(
            value["ephemeris"]
        )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEphemerisRequest:
    out: CreateEphemerisRequest = {}  # type: ignore[typeddict-item]
    if data.get("satelliteId") is not None:
        out["satellite_id"] = data["satelliteId"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("expirationTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["expiration_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("ephemeris") is not None:
        import capo_groundstation.types.ephemeris_data

        out["ephemeris"] = capo_groundstation.types.ephemeris_data.deserialize_json(
            data["ephemeris"]
        )
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    return out
