"""Generated from Smithy shape ``com.amazonaws.appconfig#GetConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.string_with_length_between1_and64
    import capo_appconfig.types.version


class GetConfigurationRequest(TypedDict, closed=True):
    application: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    """<p>The application to get. Specify either the application name or the application ID.</p>"""
    environment: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    """<p>The environment to get. Specify either the environment name or the environment ID.</p>"""
    configuration: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    """<p>The configuration to get. Specify either the configuration name or the configuration ID.</p>"""
    client_id: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    """<p>The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy. </p>"""
    client_configuration_version: NotRequired["capo_appconfig.types.version.Version"]
    """<p>The configuration version returned in the most recent <a>GetConfiguration</a> response.</p> <important> <p>AppConfig uses the value of the <code>ClientConfigurationVersion</code> parameter to identify the configuration version on your clients. If you don’t send <code>ClientConfigurationVersion</code> with each call to <a>GetConfiguration</a>, your clients receive the current configuration. You are charged each time your clients receive a configuration.</p> <p>To avoid excess charges, we recommend you use the <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html">StartConfigurationSession</a> and <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html">GetLatestConfiguration</a> APIs, which track the client configuration version on your behalf. If you choose to continue using <a>GetConfiguration</a>, we recommend that you include the <code>ClientConfigurationVersion</code> value with every call to <a>GetConfiguration</a>. The value to use for <code>ClientConfigurationVersion</code> comes from the <code>ConfigurationVersion</code> attribute returned by <a>GetConfiguration</a> when there is new or updated data, and should be saved for subsequent calls to <a>GetConfiguration</a>.</p> </important> <p>For more information about working with configurations, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html">Retrieving feature flags and configuration data in AppConfig</a> in the <i>AppConfig User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationRequest:
    out: GetConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
