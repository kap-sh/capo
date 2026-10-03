"""Generated from Smithy shape ``com.amazonaws.ivs#AdConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_arn
    import capo_ivs.types.ad_configuration_name
    import capo_ivs.types.media_tailor_playback_configurations_list
    import capo_ivs.types.post_roll_configuration
    import capo_ivs.types.tags


class AdConfiguration(TypedDict, closed=True):
    arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn"
    """<p>Ad configuration ARN.</p>"""
    name: NotRequired["capo_ivs.types.ad_configuration_name.AdConfigurationName"]
    """<p>Ad configuration name. Defaults to “”.</p>"""
    media_tailor_playback_configurations: "capo_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
    """<p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html">Generate and Sign IVS Playback Tokens</a>.</p>"""
    post_roll_configuration: NotRequired[
        "capo_ivs.types.post_roll_configuration.PostRollConfiguration"
    ]
    """<p>Configuration for the post-roll ad break to use for this ad configuration.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_ivs.types.media_tailor_playback_configurations_list

    out["mediaTailorPlaybackConfigurations"] = (
        capo_ivs.types.media_tailor_playback_configurations_list.serialize_json(
            value["media_tailor_playback_configurations"]
        )
    )
    if "post_roll_configuration" in value:
        import capo_ivs.types.post_roll_configuration

        out["postRollConfiguration"] = (
            capo_ivs.types.post_roll_configuration.serialize_json(
                value["post_roll_configuration"]
            )
        )
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AdConfiguration:
    out: AdConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AdConfiguration.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("mediaTailorPlaybackConfigurations") is not None:
        import capo_ivs.types.media_tailor_playback_configurations_list

        out["media_tailor_playback_configurations"] = (
            capo_ivs.types.media_tailor_playback_configurations_list.deserialize_json(
                data["mediaTailorPlaybackConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "AdConfiguration.media_tailor_playback_configurations required"
        )
    if data.get("postRollConfiguration") is not None:
        import capo_ivs.types.post_roll_configuration

        out["post_roll_configuration"] = (
            capo_ivs.types.post_roll_configuration.deserialize_json(
                data["postRollConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
