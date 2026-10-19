"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_repostspace.types.channel_description
    import capo_repostspace.types.channel_id
    import capo_repostspace.types.channel_name
    import capo_repostspace.types.channel_status
    import capo_repostspace.types.group_count
    import capo_repostspace.types.space_id
    import capo_repostspace.types.user_count


class ChannelData(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "capo_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""
    channel_name: "capo_repostspace.types.channel_name.ChannelName"
    """<p>The name for the channel. This must be unique per private re:Post.</p>"""
    channel_description: NotRequired[
        "capo_repostspace.types.channel_description.ChannelDescription"
    ]
    """<p>A description for the channel. This is used only to help you identify this channel.</p>"""
    create_date_time: "datetime.datetime"
    """<p>The date when the channel was created.</p>"""
    delete_date_time: NotRequired["datetime.datetime"]
    """<p>The date when the channel was deleted.</p>"""
    channel_status: "capo_repostspace.types.channel_status.ChannelStatus"
    """<p>The status pf the channel.</p>"""
    user_count: "capo_repostspace.types.user_count.UserCount"
    """<p>The number of users that are part of the channel.</p>"""
    group_count: "capo_repostspace.types.group_count.GroupCount"
    """<p>The number of groups that are part of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelData) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["channelId"] = value["channel_id"]
    out["channelName"] = value["channel_name"]
    if "channel_description" in value:
        out["channelDescription"] = value["channel_description"]
    import capo_repostspace._protocol.serialize

    out["createDateTime"] = capo_repostspace._protocol.serialize.fmt_date_time(
        value["create_date_time"]
    )
    if "delete_date_time" in value:
        import capo_repostspace._protocol.serialize

        out["deleteDateTime"] = capo_repostspace._protocol.serialize.fmt_date_time(
            value["delete_date_time"]
        )
    import capo_repostspace.types.channel_status

    out["channelStatus"] = capo_repostspace.types.channel_status.serialize_json(
        value["channel_status"]
    )
    out["userCount"] = value["user_count"]
    out["groupCount"] = value["group_count"]
    return out


def deserialize_json(data: dict) -> ChannelData:
    out: ChannelData = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = ""
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    else:
        out["channel_name"] = ""
    if data.get("channelDescription") is not None:
        out["channel_description"] = data["channelDescription"]
    if data.get("createDateTime") is not None:
        import datetime

        out["create_date_time"] = datetime.datetime.fromisoformat(
            data["createDateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("deleteDateTime") is not None:
        import datetime

        out["delete_date_time"] = datetime.datetime.fromisoformat(
            data["deleteDateTime"].replace("Z", "+00:00")
        )
    if data.get("channelStatus") is not None:
        import capo_repostspace.types.channel_status

        out["channel_status"] = capo_repostspace.types.channel_status.deserialize_json(
            data["channelStatus"]
        )
    else:
        import typing

        out["channel_status"] = typing.cast(
            "capo_repostspace.types.channel_status.ChannelStatus", ""
        )
    if data.get("userCount") is not None:
        out["user_count"] = data["userCount"]
    else:
        out["user_count"] = 0
    if data.get("groupCount") is not None:
        out["group_count"] = data["groupCount"]
    else:
        out["group_count"] = 0
    return out


def redact_sensitive(value: ChannelData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_name" in value:
        out["channel_name"] = "*** Sensitive Data Redacted ***"
    if "channel_description" in value:
        out["channel_description"] = "*** Sensitive Data Redacted ***"
    return out
