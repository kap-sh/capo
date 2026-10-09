"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#AWSAcuityReader``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_kinesis_video_archived_media._auth._signers
import capo_kinesis_video_archived_media._auth._sigv4
from capo_kinesis_video_archived_media._auth._identity import Credentials
from capo_kinesis_video_archived_media._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis_video_archived_media._auth._zapros_handler import AuthMiddleware
from capo_kinesis_video_archived_media._pagination import resolve_path as _resolve_path
from capo_kinesis_video_archived_media._services._aws_config import aws_config
from capo_kinesis_video_archived_media._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.clip_fragment_selector
    import capo_kinesis_video_archived_media.types.container_format
    import capo_kinesis_video_archived_media.types.dash_display_fragment_number
    import capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp
    import capo_kinesis_video_archived_media.types.dash_fragment_selector
    import capo_kinesis_video_archived_media.types.dash_max_results
    import capo_kinesis_video_archived_media.types.dash_playback_mode
    import capo_kinesis_video_archived_media.types.expires
    import capo_kinesis_video_archived_media.types.format
    import capo_kinesis_video_archived_media.types.format_config
    import capo_kinesis_video_archived_media.types.fragment
    import capo_kinesis_video_archived_media.types.fragment_number_list
    import capo_kinesis_video_archived_media.types.fragment_selector
    import capo_kinesis_video_archived_media.types.get_clip_input
    import capo_kinesis_video_archived_media.types.get_clip_output
    import capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_input
    import capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_output
    import capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_input
    import capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_output
    import capo_kinesis_video_archived_media.types.get_images_input
    import capo_kinesis_video_archived_media.types.get_images_max_results
    import capo_kinesis_video_archived_media.types.get_images_output
    import capo_kinesis_video_archived_media.types.get_media_for_fragment_list_input
    import capo_kinesis_video_archived_media.types.get_media_for_fragment_list_output
    import capo_kinesis_video_archived_media.types.height_pixels
    import capo_kinesis_video_archived_media.types.hls_discontinuity_mode
    import capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp
    import capo_kinesis_video_archived_media.types.hls_fragment_selector
    import capo_kinesis_video_archived_media.types.hls_max_results
    import capo_kinesis_video_archived_media.types.hls_playback_mode
    import capo_kinesis_video_archived_media.types.image
    import capo_kinesis_video_archived_media.types.image_selector_type
    import capo_kinesis_video_archived_media.types.list_fragments_input
    import capo_kinesis_video_archived_media.types.list_fragments_max_results
    import capo_kinesis_video_archived_media.types.list_fragments_output
    import capo_kinesis_video_archived_media.types.next_token
    import capo_kinesis_video_archived_media.types.resource_arn
    import capo_kinesis_video_archived_media.types.sampling_interval
    import capo_kinesis_video_archived_media.types.stream_name
    import capo_kinesis_video_archived_media.types.timestamp
    import capo_kinesis_video_archived_media.types.width_pixels


class KinesisVideoArchivedMediaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class KinesisVideoArchivedMediaClient:
    """A client for the ``KinesisVideoArchivedMedia`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = KinesisVideoArchivedMediaClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KinesisVideoArchivedMediaClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    @contextmanager
    def get_clip(
        self,
        clip_fragment_selector: "capo_kinesis_video_archived_media.types.clip_fragment_selector.ClipFragmentSelector",
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "Generator[capo_kinesis_video_archived_media.types.get_clip_output.GetClipOutput]":
        """<p>Downloads an MP4 file (clip) containing the archived, on-demand media from the specified video stream over the specified time range. </p> <p>Both the StreamName and the StreamARN parameters are optional, but you must specify either the StreamName or the StreamARN when invoking this API operation. </p> <p>As a prerequisite to using GetCLip API, you must obtain an endpoint using <code>GetDataEndpoint</code>, specifying GET_CLIP for<code></code> the <code>APIName</code> parameter. </p> <p>An Amazon Kinesis video stream has the following requirements for providing data through MP4:</p> <ul> <li> <p>The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio. Specifically, the codec ID of track 1 should be <code>V_MPEG/ISO/AVC</code> (for h.264) or V_MPEGH/ISO/HEVC (for H.265). Optionally, the codec ID of track 2 should be <code>A_AAC</code> (for AAC) or A_MS/ACM (for G.711).</p> </li> <li> <p>Data retention must be greater than 0.</p> </li> <li> <p>The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more information, see <a href="https://www.iso.org/standard/55980.html">MPEG-4 specification ISO/IEC 14496-15</a>. For information about adapting stream data to a given format, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html">NAL Adaptation Flags</a>.</p> </li> <li> <p>The audio track (if present) of each fragment must contain codec private data in the AAC format (<a href="https://www.iso.org/standard/43345.html">AAC specification ISO/IEC 13818-7</a>) or the <a href="http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html">MS Wave format</a>.</p> </li> </ul> <p>You can monitor the amount of outgoing data by monitoring the <code>GetClip.OutgoingBytes</code> Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html">Monitoring Kinesis Video Streams</a>. For pricing information, see <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Amazon Kinesis Video Streams Pricing</a> and <a href="https://aws.amazon.com/pricing/"> Amazon Web Services Pricing</a>. Charges for outgoing Amazon Web Services data apply.</p>

        Args:
            stream_name: <p>The name of the stream for which to retrieve the media clip. </p> <p>You must specify either the StreamName or the StreamARN. </p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for which to retrieve the media clip. </p> <p>You must specify either the StreamName or the StreamARN. </p>
            clip_fragment_selector: <p>The time range of the requested clip and the source of the timestamps.</p>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.invalid_codec_private_data_exception.InvalidCodecPrivateDataException: <p>The codec private data in at least one of the tracks of the video stream is not valid for this operation.</p>
            capo_kinesis_video_archived_media.errors.invalid_media_frame_exception.InvalidMediaFrameException: <p>One or more frames in the requested clip could not be parsed based on the specified codec.</p>
            capo_kinesis_video_archived_media.errors.missing_codec_private_data_exception.MissingCodecPrivateDataException: <p>No codec private data was found in at least one of tracks of the video stream.</p>
            capo_kinesis_video_archived_media.errors.no_data_retention_exception.NoDataRetentionException: <p> <code>GetImages</code> was requested for a stream that does not retain data (that is, has a <code>DataRetentionInHours</code> of 0). </p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.unsupported_stream_media_type_exception.UnsupportedStreamMediaTypeException: <p>The type of the media (for example, h.264 or h.265 video or ACC or G.711 audio) could not be determined from the codec IDs of the tracks in the first fragment for a playback session. The codec ID for track 1 should be <code>V_MPEG/ISO/AVC</code> and, optionally, the codec ID for track 2 should be <code>A_AAC</code>.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.get_clip_input.GetClipInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.get_clip_output.GetClipOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_clip

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_clip.get_clip(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.get_clip_input.GetClipInput = {
            "clip_fragment_selector": clip_fragment_selector
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def get_dash_streaming_session_url(
        self,
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        playback_mode: Optional[
            "capo_kinesis_video_archived_media.types.dash_playback_mode.DASHPlaybackMode"
        ] = None,
        display_fragment_timestamp: Optional[
            "capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp.DASHDisplayFragmentTimestamp"
        ] = None,
        display_fragment_number: Optional[
            "capo_kinesis_video_archived_media.types.dash_display_fragment_number.DASHDisplayFragmentNumber"
        ] = None,
        dash_fragment_selector: Optional[
            "capo_kinesis_video_archived_media.types.dash_fragment_selector.DASHFragmentSelector"
        ] = None,
        expires: Optional[
            "capo_kinesis_video_archived_media.types.expires.Expires"
        ] = None,
        max_manifest_fragment_results: Optional[
            "capo_kinesis_video_archived_media.types.dash_max_results.DASHMaxResults"
        ] = None,
    ) -> "capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_output.GetDASHStreamingSessionURLOutput":
        """<p>Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream. You can then open the URL in a media player to view the stream contents.</p> <p>Both the <code>StreamName</code> and the <code>StreamARN</code> parameters are optional, but you must specify either the <code>StreamName</code> or the <code>StreamARN</code> when invoking this API operation.</p> <p>An Amazon Kinesis video stream has the following requirements for providing data through MPEG-DASH:</p> <ul> <li> <p>The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio. Specifically, the codec ID of track 1 should be <code>V_MPEG/ISO/AVC</code> (for h.264) or V_MPEGH/ISO/HEVC (for H.265). Optionally, the codec ID of track 2 should be <code>A_AAC</code> (for AAC) or A_MS/ACM (for G.711).</p> </li> <li> <p>Data retention must be greater than 0.</p> </li> <li> <p>The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more information, see <a href="https://www.iso.org/standard/55980.html">MPEG-4 specification ISO/IEC 14496-15</a>. For information about adapting stream data to a given format, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html">NAL Adaptation Flags</a>.</p> </li> <li> <p>The audio track (if present) of each fragment must contain codec private data in the AAC format (<a href="https://www.iso.org/standard/43345.html">AAC specification ISO/IEC 13818-7</a>) or the <a href="http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html">MS Wave format</a>.</p> </li> </ul> <p>The following procedure shows how to use MPEG-DASH with Kinesis Video Streams:</p> <ol> <li> <p>Get an endpoint using <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html">GetDataEndpoint</a>, specifying <code>GET_DASH_STREAMING_SESSION_URL</code> for the <code>APIName</code> parameter.</p> </li> <li> <p>Retrieve the MPEG-DASH URL using <code>GetDASHStreamingSessionURL</code>. Kinesis Video Streams creates an MPEG-DASH streaming session to be used for accessing content in a stream using the MPEG-DASH protocol. <code>GetDASHStreamingSessionURL</code> returns an authenticated URL (that includes an encrypted session token) for the session's MPEG-DASH <i>manifest</i> (the root resource needed for streaming with MPEG-DASH).</p> <note> <p>Don't share or store this token where an unauthorized entity can access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you use with your Amazon Web Services credentials.</p> </note> <p>The media that is made available through the manifest consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.</p> </li> <li> <p>Provide the URL (containing the encrypted session token) for the MPEG-DASH manifest to a media player that supports the MPEG-DASH protocol. Kinesis Video Streams makes the initialization fragment and media fragments available through the manifest URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain encoded video frames or encoded audio samples.</p> </li> <li> <p>The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:</p> <ul> <li> <p> <b>GetDASHManifest:</b> Retrieves an MPEG DASH manifest, which contains the metadata for the media that you want to playback.</p> </li> <li> <p> <b>GetMP4InitFragment:</b> Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the "<code>fytp</code>" and "<code>moov</code>" MP4 atoms, and the child atoms that are needed to initialize the media player decoder.</p> <p>The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.</p> </li> <li> <p> <b>GetMP4MediaFragment:</b> Retrieves MP4 media fragments. These fragments contain the "<code>moof</code>" and "<code>mdat</code>" MP4 atoms and their child atoms, containing the encoded fragment's media frames and their timestamps. </p> <note> <p>After the first media fragment is made available in a streaming session, any fragments that don't contain the same codec private data cause an error to be returned when those different media fragments are loaded. Therefore, the codec private data should not change between fragments in a session. This also means that the session fails if the fragments in a stream change from having only video to having both audio and video.</p> </note> <p>Data retrieved with this action is billable. See <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Pricing</a> for details.</p> </li> </ul> </li> </ol> <note> <p>For restrictions that apply to MPEG-DASH sessions, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p> </note> <p>You can monitor the amount of data that the media player consumes by monitoring the <code>GetMP4MediaFragment.OutgoingBytes</code> Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html">Monitoring Kinesis Video Streams</a>. For pricing information, see <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Amazon Kinesis Video Streams Pricing</a> and <a href="https://aws.amazon.com/pricing/">Amazon Web Services Pricing</a>. Charges for both HLS sessions and outgoing Amazon Web Services data apply.</p> <p>For more information about HLS, see <a href="https://developer.apple.com/streaming/">HTTP Live Streaming</a> on the <a href="https://developer.apple.com">Apple Developer site</a>.</p> <important> <p>If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: </p> <ul> <li> <p> <code>x-amz-ErrorType</code> HTTP header – contains a more specific error type in addition to what the HTTP status code provides. </p> </li> <li> <p> <code>x-amz-RequestId</code> HTTP header – if you want to report an issue to Amazon Web Services the support team can better diagnose the problem if given the Request Id.</p> </li> </ul> <p>Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.</p> <p>For more information, see the <b>Errors</b> section at the bottom of this topic, as well as <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html">Common Errors</a>. </p> </important>

        Args:
            stream_name: <p>The name of the stream for which to retrieve the MPEG-DASH manifest URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for which to retrieve the MPEG-DASH manifest URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            playback_mode: <p>Whether to retrieve live, live replay, or archived, on-demand data.</p> <p>Features of the three types of sessions include the following:</p> <ul> <li> <p> <b> <code>LIVE</code> </b>: For sessions of this type, the MPEG-DASH manifest is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new manifest on a one-second interval. When this type of session is played in a media player, the user interface typically displays a "live" notification, with no scrubber control for choosing the position in the playback window to display.</p> <note> <p>In <code>LIVE</code> mode, the newest available fragments are included in an MPEG-DASH manifest, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the MPEG-DASH manifest if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the manifest, the older fragment is not added, and the gap is not filled.</p> </note> </li> <li> <p> <b> <code>LIVE_REPLAY</code> </b>: For sessions of this type, the MPEG-DASH manifest is updated similarly to how it is updated for <code>LIVE</code> mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the manifest every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the <code>ON_DEMAND</code> mode. </p> </li> <li> <p> <b> <code>ON_DEMAND</code> </b>: For sessions of this type, the MPEG-DASH manifest contains all the fragments for the session, up to the number that is specified in <code>MaxManifestFragmentResults</code>. The manifest must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.</p> </li> </ul> <p>In all playback modes, if <code>FragmentSelectorType</code> is <code>PRODUCER_TIMESTAMP</code>, and if there are multiple fragments with the same start timestamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the MPEG-DASH manifest. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the MPEG-DASH manifest. This can lead to unexpected behavior in the media player.</p> <p>The default is <code>LIVE</code>.</p>
            display_fragment_timestamp: <p>Per the MPEG-DASH specification, the wall-clock time of fragments in the manifest file can be derived using attributes in the manifest itself. However, typically, MPEG-DASH compatible media players do not properly handle gaps in the media timeline. Kinesis Video Streams adjusts the media timeline in the manifest file to enable playback of media with discontinuities. Therefore, the wall-clock time derived from the manifest file may be inaccurate. If DisplayFragmentTimestamp is set to <code>ALWAYS</code>, the accurate fragment timestamp is added to each S element in the manifest file with the attribute name “kvs:ts”. A custom MPEG-DASH media player is necessary to leverage this custom attribute.</p> <p>The default value is <code>NEVER</code>. When <a>DASHFragmentSelector</a> is <code>SERVER_TIMESTAMP</code>, the timestamps will be the server start timestamps. Similarly, when <a>DASHFragmentSelector</a> is <code>PRODUCER_TIMESTAMP</code>, the timestamps will be the producer start timestamps. </p>
            display_fragment_number: <p>Fragments are identified in the manifest file based on their sequence number in the session. If DisplayFragmentNumber is set to <code>ALWAYS</code>, the Kinesis Video Streams fragment number is added to each S element in the manifest file with the attribute name “kvs:fn”. These fragment numbers can be used for logging or for use with other APIs (e.g. <code>GetMedia</code> and <code>GetMediaForFragmentList</code>). A custom MPEG-DASH media player is necessary to leverage these this custom attribute.</p> <p>The default value is <code>NEVER</code>.</p>
            dash_fragment_selector: <p>The time range of the requested fragment and the source of the timestamps.</p> <p>This parameter is required if <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>. This parameter is optional if PlaybackMode is<code></code> <code>LIVE</code>. If <code>PlaybackMode</code> is <code>LIVE</code>, the <code>FragmentSelectorType</code> can be set, but the <code>TimestampRange</code> should not be set. If <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>, both <code>FragmentSelectorType</code> and <code>TimestampRange</code> must be set.</p>
            expires: <p>The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).</p> <p>When a session expires, no new calls to <code>GetDashManifest</code>, <code>GetMP4InitFragment</code>, or <code>GetMP4MediaFragment</code> can be made for that session.</p> <p>The default is 300 (5 minutes).</p>
            max_manifest_fragment_results: <p>The maximum number of fragments that are returned in the MPEG-DASH manifest.</p> <p>When the <code>PlaybackMode</code> is <code>LIVE</code>, the most recent fragments are returned up to this value. When the <code>PlaybackMode</code> is <code>ON_DEMAND</code>, the oldest fragments are returned, up to this maximum number.</p> <p>When there are a higher number of fragments available in a live MPEG-DASH manifest, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live MPEG-DASH manifest have a minimum of 3 fragments and a maximum of 10 fragments.</p> <p>The default is 5 fragments if <code>PlaybackMode</code> is <code>LIVE</code> or <code>LIVE_REPLAY</code>, and 1,000 if <code>PlaybackMode</code> is <code>ON_DEMAND</code>. </p> <p>The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.</p>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.invalid_codec_private_data_exception.InvalidCodecPrivateDataException: <p>The codec private data in at least one of the tracks of the video stream is not valid for this operation.</p>
            capo_kinesis_video_archived_media.errors.missing_codec_private_data_exception.MissingCodecPrivateDataException: <p>No codec private data was found in at least one of tracks of the video stream.</p>
            capo_kinesis_video_archived_media.errors.no_data_retention_exception.NoDataRetentionException: <p> <code>GetImages</code> was requested for a stream that does not retain data (that is, has a <code>DataRetentionInHours</code> of 0). </p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.unsupported_stream_media_type_exception.UnsupportedStreamMediaTypeException: <p>The type of the media (for example, h.264 or h.265 video or ACC or G.711 audio) could not be determined from the codec IDs of the tracks in the first fragment for a playback session. The codec ID for track 1 should be <code>V_MPEG/ISO/AVC</code> and, optionally, the codec ID for track 2 should be <code>A_AAC</code>.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_input.GetDASHStreamingSessionURLInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_output.GetDASHStreamingSessionURLOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_dash_streaming_session_url

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_dash_streaming_session_url.get_dash_streaming_session_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.get_dash_streaming_session_url_input.GetDASHStreamingSessionURLInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if playback_mode is not None:
            input_["playback_mode"] = playback_mode
        if display_fragment_timestamp is not None:
            input_["display_fragment_timestamp"] = display_fragment_timestamp
        if display_fragment_number is not None:
            input_["display_fragment_number"] = display_fragment_number
        if dash_fragment_selector is not None:
            input_["dash_fragment_selector"] = dash_fragment_selector
        if expires is not None:
            input_["expires"] = expires
        if max_manifest_fragment_results is not None:
            input_["max_manifest_fragment_results"] = max_manifest_fragment_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hls_streaming_session_url(
        self,
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        playback_mode: Optional[
            "capo_kinesis_video_archived_media.types.hls_playback_mode.HLSPlaybackMode"
        ] = None,
        hls_fragment_selector: Optional[
            "capo_kinesis_video_archived_media.types.hls_fragment_selector.HLSFragmentSelector"
        ] = None,
        container_format: Optional[
            "capo_kinesis_video_archived_media.types.container_format.ContainerFormat"
        ] = None,
        discontinuity_mode: Optional[
            "capo_kinesis_video_archived_media.types.hls_discontinuity_mode.HLSDiscontinuityMode"
        ] = None,
        display_fragment_timestamp: Optional[
            "capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp.HLSDisplayFragmentTimestamp"
        ] = None,
        expires: Optional[
            "capo_kinesis_video_archived_media.types.expires.Expires"
        ] = None,
        max_media_playlist_fragment_results: Optional[
            "capo_kinesis_video_archived_media.types.hls_max_results.HLSMaxResults"
        ] = None,
    ) -> "capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_output.GetHLSStreamingSessionURLOutput":
        """<p>Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser or media player to view the stream contents.</p> <p>Both the <code>StreamName</code> and the <code>StreamARN</code> parameters are optional, but you must specify either the <code>StreamName</code> or the <code>StreamARN</code> when invoking this API operation.</p> <p>An Amazon Kinesis video stream has the following requirements for providing data through HLS:</p> <ul> <li> <p>For streaming video, the media must contain H.264 or H.265 encoded video and, optionally, AAC encoded audio. Specifically, the codec ID of track 1 should be <code>V_MPEG/ISO/AVC</code> (for H.264) or <code>V_MPEG/ISO/HEVC</code> (for H.265). Optionally, the codec ID of track 2 should be <code>A_AAC</code>. For audio only streaming, the codec ID of track 1 should be <code>A_AAC</code>.</p> </li> <li> <p>Data retention must be greater than 0.</p> </li> <li> <p>The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format or HEVC for H.265 format (<a href="https://www.iso.org/standard/55980.html">MPEG-4 specification ISO/IEC 14496-15</a>). For information about adapting stream data to a given format, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html">NAL Adaptation Flags</a>.</p> </li> <li> <p>The audio track (if present) of each fragment must contain codec private data in the AAC format (<a href="https://www.iso.org/standard/43345.html">AAC specification ISO/IEC 13818-7</a>).</p> </li> </ul> <p>Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called fMP4 or CMAF) or the MPEG-2 form (also called TS chunks, which the HLS specification also supports). For more information about HLS fragment types, see the <a href="https://tools.ietf.org/html/draft-pantos-http-live-streaming-23">HLS specification</a>.</p> <p>The following procedure shows how to use HLS with Kinesis Video Streams:</p> <ol> <li> <p>Get an endpoint using <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html">GetDataEndpoint</a>, specifying <code>GET_HLS_STREAMING_SESSION_URL</code> for the <code>APIName</code> parameter.</p> </li> <li> <p>Retrieve the HLS URL using <code>GetHLSStreamingSessionURL</code>. Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. <code>GetHLSStreamingSessionURL</code> returns an authenticated URL (that includes an encrypted session token) for the session's HLS <i>master playlist</i> (the root resource needed for streaming with HLS).</p> <note> <p>Don't share or store this token where an unauthorized entity could access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you would use with your Amazon Web Services credentials.</p> </note> <p>The media that is made available through the playlist consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.</p> </li> <li> <p>Provide the URL (containing the encrypted session token) for the HLS master playlist to a media player that supports the HLS protocol. Kinesis Video Streams makes the HLS media playlist, initialization fragment, and media fragments available through the master playlist URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain H.264-encoded video frames or AAC-encoded audio samples.</p> </li> <li> <p>The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:</p> <ul> <li> <p> <b>GetHLSMasterPlaylist:</b> Retrieves an HLS master playlist, which contains a URL for the <code>GetHLSMediaPlaylist</code> action for each track, and additional metadata for the media player, including estimated bitrate and resolution.</p> </li> <li> <p> <b>GetHLSMediaPlaylist:</b> Retrieves an HLS media playlist, which contains a URL to access the MP4 initialization fragment with the <code>GetMP4InitFragment</code> action, and URLs to access the MP4 media fragments with the <code>GetMP4MediaFragment</code> actions. The HLS media playlist also contains metadata about the stream that the player needs to play it, such as whether the <code>PlaybackMode</code> is <code>LIVE</code> or <code>ON_DEMAND</code>. The HLS media playlist is typically static for sessions with a <code>PlaybackType</code> of <code>ON_DEMAND</code>. The HLS media playlist is continually updated with new fragments for sessions with a <code>PlaybackType</code> of <code>LIVE</code>. There is a distinct HLS media playlist for the video track and the audio track (if applicable) that contains MP4 media URLs for the specific track. </p> </li> <li> <p> <b>GetMP4InitFragment:</b> Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the "<code>fytp</code>" and "<code>moov</code>" MP4 atoms, and the child atoms that are needed to initialize the media player decoder.</p> <p>The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.</p> </li> <li> <p> <b>GetMP4MediaFragment:</b> Retrieves MP4 media fragments. These fragments contain the "<code>moof</code>" and "<code>mdat</code>" MP4 atoms and their child atoms, containing the encoded fragment's media frames and their timestamps. </p> <note> <p>For the HLS streaming session, in-track codec private data (CPD) changes are supported. After the first media fragment is made available in a streaming session, fragments can contain CPD changes for each track. Therefore, the fragments in a session can have a different resolution, bit rate, or other information in the CPD without interrupting playback. However, any change made in the track number or track codec format can return an error when those different media fragments are loaded. For example, streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an ALAW audio track. For each streaming session, only 500 CPD changes are allowed.</p> </note> <p>Data retrieved with this action is billable. For information, see <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Pricing</a>.</p> </li> <li> <p> <b>GetTSFragment:</b> Retrieves MPEG TS fragments containing both initialization and media data for all tracks in the stream.</p> <note> <p>If the <code>ContainerFormat</code> is <code>MPEG_TS</code>, this API is used instead of <code>GetMP4InitFragment</code> and <code>GetMP4MediaFragment</code> to retrieve stream media.</p> </note> <p>Data retrieved with this action is billable. For more information, see <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Kinesis Video Streams pricing</a>.</p> </li> </ul> </li> </ol> <p>A streaming session URL must not be shared between players. The service might throttle a session if multiple media players are sharing it. For connection limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p> <p>You can monitor the amount of data that the media player consumes by monitoring the <code>GetMP4MediaFragment.OutgoingBytes</code> Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html">Monitoring Kinesis Video Streams</a>. For pricing information, see <a href="https://aws.amazon.com/kinesis/video-streams/pricing/">Amazon Kinesis Video Streams Pricing</a> and <a href="https://aws.amazon.com/pricing/">Amazon Web Services Pricing</a>. Charges for both HLS sessions and outgoing Amazon Web Services data apply.</p> <p>For more information about HLS, see <a href="https://developer.apple.com/streaming/">HTTP Live Streaming</a> on the <a href="https://developer.apple.com">Apple Developer site</a>.</p> <important> <p>If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: </p> <ul> <li> <p> <code>x-amz-ErrorType</code> HTTP header – contains a more specific error type in addition to what the HTTP status code provides. </p> </li> <li> <p> <code>x-amz-RequestId</code> HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.</p> </li> </ul> <p>Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.</p> <p>For more information, see the <b>Errors</b> section at the bottom of this topic, as well as <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html">Common Errors</a>. </p> </important>

        Args:
            stream_name: <p>The name of the stream for which to retrieve the HLS master playlist URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            playback_mode: <p>Whether to retrieve live, live replay, or archived, on-demand data.</p> <p>Features of the three types of sessions include the following:</p> <ul> <li> <p> <b> <code>LIVE</code> </b>: For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a "live" notification, with no scrubber control for choosing the position in the playback window to display.</p> <note> <p>In <code>LIVE</code> mode, the newest available fragments are included in an HLS media playlist, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the HLS media playlist if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the playlist, the older fragment is not added, and the gap is not filled.</p> </note> </li> <li> <p> <b> <code>LIVE_REPLAY</code> </b>: For sessions of this type, the HLS media playlist is updated similarly to how it is updated for <code>LIVE</code> mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the media playlist every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the <code>ON_DEMAND</code> mode. </p> </li> <li> <p> <b> <code>ON_DEMAND</code> </b>: For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in <code>MaxMediaPlaylistFragmentResults</code>. The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.</p> </li> </ul> <p>In all playback modes, if <code>FragmentSelectorType</code> is <code>PRODUCER_TIMESTAMP</code>, and if there are multiple fragments with the same start timestamp, the fragment that has the largest fragment number (that is, the newest fragment) is included in the HLS media playlist. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the HLS media playlist. This can lead to unexpected behavior in the media player.</p> <p>The default is <code>LIVE</code>.</p>
            hls_fragment_selector: <p>The time range of the requested fragment and the source of the timestamps.</p> <p>This parameter is required if <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>. This parameter is optional if PlaybackMode is<code></code> <code>LIVE</code>. If <code>PlaybackMode</code> is <code>LIVE</code>, the <code>FragmentSelectorType</code> can be set, but the <code>TimestampRange</code> should not be set. If <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>, both <code>FragmentSelectorType</code> and <code>TimestampRange</code> must be set.</p>
            container_format: <p>Specifies which format should be used for packaging the media. Specifying the <code>FRAGMENTED_MP4</code> container format packages the media into MP4 fragments (fMP4 or CMAF). This is the recommended packaging because there is minimal packaging overhead. The other container format option is <code>MPEG_TS</code>. HLS has supported MPEG TS chunks since it was released and is sometimes the only supported packaging on older HLS players. MPEG TS typically has a 5-25 percent packaging overhead. This means MPEG TS typically requires 5-25 percent more bandwidth and cost than fMP4.</p> <p>The default is <code>FRAGMENTED_MP4</code>.</p>
            discontinuity_mode: <p>Specifies when flags marking discontinuities between fragments are added to the media playlists.</p> <p>Media players typically build a timeline of media content to play, based on the timestamps of each fragment. This means that if there is any overlap or gap between fragments (as is typical if <a>HLSFragmentSelector</a> is set to <code>SERVER_TIMESTAMP</code>), the media player timeline will also have small gaps between fragments in some places, and will overwrite frames in other places. Gaps in the media player timeline can cause playback to stall and overlaps can cause playback to be jittery. When there are discontinuity flags between fragments, the media player is expected to reset the timeline, resulting in the next fragment being played immediately after the previous fragment. </p> <p>The following modes are supported:</p> <ul> <li> <p> <code>ALWAYS</code>: a discontinuity marker is placed between every fragment in the HLS media playlist. It is recommended to use a value of <code>ALWAYS</code> if the fragment timestamps are not accurate.</p> </li> <li> <p> <code>NEVER</code>: no discontinuity markers are placed anywhere. It is recommended to use a value of <code>NEVER</code> to ensure the media player timeline most accurately maps to the producer timestamps. </p> </li> <li> <p> <code>ON_DISCONTINUITY</code>: a discontinuity marker is placed between fragments that have a gap or overlap of more than 50 milliseconds. For most playback scenarios, it is recommended to use a value of <code>ON_DISCONTINUITY</code> so that the media player timeline is only reset when there is a significant issue with the media timeline (e.g. a missing fragment).</p> </li> </ul> <p>The default is <code>ALWAYS</code> when <a>HLSFragmentSelector</a> is set to <code>SERVER_TIMESTAMP</code>, and <code>NEVER</code> when it is set to <code>PRODUCER_TIMESTAMP</code>.</p>
            display_fragment_timestamp: <p>Specifies when the fragment start timestamps should be included in the HLS media playlist. Typically, media players report the playhead position as a time relative to the start of the first fragment in the playback session. However, when the start timestamps are included in the HLS media playlist, some media players might report the current playhead as an absolute time based on the fragment timestamps. This can be useful for creating a playback experience that shows viewers the wall-clock time of the media.</p> <p>The default is <code>NEVER</code>. When <a>HLSFragmentSelector</a> is <code>SERVER_TIMESTAMP</code>, the timestamps will be the server start timestamps. Similarly, when <a>HLSFragmentSelector</a> is <code>PRODUCER_TIMESTAMP</code>, the timestamps will be the producer start timestamps. </p>
            expires: <p>The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).</p> <p>When a session expires, no new calls to <code>GetHLSMasterPlaylist</code>, <code>GetHLSMediaPlaylist</code>, <code>GetMP4InitFragment</code>, <code>GetMP4MediaFragment</code>, or <code>GetTSFragment</code> can be made for that session.</p> <p>The default is 300 (5 minutes).</p>
            max_media_playlist_fragment_results: <p>The maximum number of fragments that are returned in the HLS media playlists.</p> <p>When the <code>PlaybackMode</code> is <code>LIVE</code>, the most recent fragments are returned up to this value. When the <code>PlaybackMode</code> is <code>ON_DEMAND</code>, the oldest fragments are returned, up to this maximum number.</p> <p>When there are a higher number of fragments available in a live HLS media playlist, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10 fragments.</p> <p>The default is 5 fragments if <code>PlaybackMode</code> is <code>LIVE</code> or <code>LIVE_REPLAY</code>, and 1,000 if <code>PlaybackMode</code> is <code>ON_DEMAND</code>. </p> <p>The maximum value of 5,000 fragments corresponds to more than 80 minutes of video on streams with 1-second fragments, and more than 13 hours of video on streams with 10-second fragments.</p>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.invalid_codec_private_data_exception.InvalidCodecPrivateDataException: <p>The codec private data in at least one of the tracks of the video stream is not valid for this operation.</p>
            capo_kinesis_video_archived_media.errors.missing_codec_private_data_exception.MissingCodecPrivateDataException: <p>No codec private data was found in at least one of tracks of the video stream.</p>
            capo_kinesis_video_archived_media.errors.no_data_retention_exception.NoDataRetentionException: <p> <code>GetImages</code> was requested for a stream that does not retain data (that is, has a <code>DataRetentionInHours</code> of 0). </p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.unsupported_stream_media_type_exception.UnsupportedStreamMediaTypeException: <p>The type of the media (for example, h.264 or h.265 video or ACC or G.711 audio) could not be determined from the codec IDs of the tracks in the first fragment for a playback session. The codec ID for track 1 should be <code>V_MPEG/ISO/AVC</code> and, optionally, the codec ID for track 2 should be <code>A_AAC</code>.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_input.GetHLSStreamingSessionURLInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_output.GetHLSStreamingSessionURLOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_hls_streaming_session_url

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_hls_streaming_session_url.get_hls_streaming_session_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.get_hls_streaming_session_url_input.GetHLSStreamingSessionURLInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if playback_mode is not None:
            input_["playback_mode"] = playback_mode
        if hls_fragment_selector is not None:
            input_["hls_fragment_selector"] = hls_fragment_selector
        if container_format is not None:
            input_["container_format"] = container_format
        if discontinuity_mode is not None:
            input_["discontinuity_mode"] = discontinuity_mode
        if display_fragment_timestamp is not None:
            input_["display_fragment_timestamp"] = display_fragment_timestamp
        if expires is not None:
            input_["expires"] = expires
        if max_media_playlist_fragment_results is not None:
            input_["max_media_playlist_fragment_results"] = (
                max_media_playlist_fragment_results
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_images(
        self,
        image_selector_type: "capo_kinesis_video_archived_media.types.image_selector_type.ImageSelectorType",
        start_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp",
        end_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp",
        format: "capo_kinesis_video_archived_media.types.format.Format",
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        sampling_interval: Optional[
            "capo_kinesis_video_archived_media.types.sampling_interval.SamplingInterval"
        ] = None,
        format_config: Optional[
            "capo_kinesis_video_archived_media.types.format_config.FormatConfig"
        ] = None,
        width_pixels: Optional[
            "capo_kinesis_video_archived_media.types.width_pixels.WidthPixels"
        ] = None,
        height_pixels: Optional[
            "capo_kinesis_video_archived_media.types.height_pixels.HeightPixels"
        ] = None,
        max_results: Optional[
            "capo_kinesis_video_archived_media.types.get_images_max_results.GetImagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_kinesis_video_archived_media.types.next_token.NextToken"
        ] = None,
    ) -> "capo_kinesis_video_archived_media.types.get_images_output.GetImagesOutput":
        """<p>Retrieves a list of images corresponding to each timestamp for a given time range, sampling interval, and image format configuration.</p>

        Args:
            stream_name: <p>The name of the stream from which to retrieve the images. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream from which to retrieve the images. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            image_selector_type: <p>The origin of the Server or Producer timestamps to use to generate the images.</p>
            start_timestamp: <p>The starting point from which the images should be generated. This <code>StartTimestamp</code> must be within an inclusive range of timestamps for an image to be returned.</p>
            end_timestamp: <p>The end timestamp for the range of images to be generated. If the time range between <code>StartTimestamp</code> and <code>EndTimestamp</code> is more than 300 seconds above <code>StartTimestamp</code>, you will receive an <code>IllegalArgumentException</code>.</p>
            sampling_interval: <p>The time interval in milliseconds (ms) at which the images need to be generated from the stream. The minimum value that can be provided is 200 ms (5 images per second). If the timestamp range is less than the sampling interval, the image from the <code>startTimestamp</code> will be returned if available. </p>
            format: <p>The format that will be used to encode the image.</p>
            format_config: <p>The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated. The <code>FormatConfig</code> key is the <code>JPEGQuality</code>, which indicates the JPEG quality key to be used to generate the image. The <code>FormatConfig</code> value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression. If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the <code>JPEGQuality</code> key will be set to 80.</p>
            width_pixels: <p>The width of the output image that is used in conjunction with the <code>HeightPixels</code> parameter. When both <code>WidthPixels</code> and <code>HeightPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>WidthPixels</code> parameter is provided or if only the <code>HeightPixels</code> is provided, a <code>ValidationException</code> will be thrown. If neither parameter is provided, the original image size from the stream will be returned.</p>
            height_pixels: <p>The height of the output image that is used in conjunction with the <code>WidthPixels</code> parameter. When both <code>HeightPixels</code> and <code>WidthPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>HeightPixels</code> parameter is provided, its original aspect ratio will be used to calculate the <code>WidthPixels</code> ratio. If neither parameter is provided, the original image size will be returned.</p>
            max_results: <p>The maximum number of images to be returned by the API. </p> <note> <p>The default limit is 25 images per API response. Providing a <code>MaxResults</code> greater than this value will result in a page size of 25. Any additional results will be paginated. </p> </note>
            next_token: <p>A token that specifies where to start paginating the next set of Images. This is the <code>GetImages:NextToken</code> from a previously truncated response.</p>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.no_data_retention_exception.NoDataRetentionException: <p> <code>GetImages</code> was requested for a stream that does not retain data (that is, has a <code>DataRetentionInHours</code> of 0). </p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.get_images_input.GetImagesInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.get_images_output.GetImagesOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_images

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_images.get_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.get_images_input.GetImagesInput = {
            "image_selector_type": image_selector_type,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "format": format,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if sampling_interval is not None:
            input_["sampling_interval"] = sampling_interval
        if format_config is not None:
            input_["format_config"] = format_config
        if width_pixels is not None:
            input_["width_pixels"] = width_pixels
        if height_pixels is not None:
            input_["height_pixels"] = height_pixels
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_images(
        self,
        image_selector_type: "capo_kinesis_video_archived_media.types.image_selector_type.ImageSelectorType",
        start_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp",
        end_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp",
        format: "capo_kinesis_video_archived_media.types.format.Format",
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        sampling_interval: Optional[
            "capo_kinesis_video_archived_media.types.sampling_interval.SamplingInterval"
        ] = None,
        format_config: Optional[
            "capo_kinesis_video_archived_media.types.format_config.FormatConfig"
        ] = None,
        width_pixels: Optional[
            "capo_kinesis_video_archived_media.types.width_pixels.WidthPixels"
        ] = None,
        height_pixels: Optional[
            "capo_kinesis_video_archived_media.types.height_pixels.HeightPixels"
        ] = None,
        max_results: Optional[
            "capo_kinesis_video_archived_media.types.get_images_max_results.GetImagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_kinesis_video_archived_media.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_kinesis_video_archived_media.types.image.Image]":
        _token = next_token
        while True:
            _response = self.get_images(
                image_selector_type,
                start_timestamp,
                end_timestamp,
                format,
                config_overrides=config_overrides,
                stream_name=stream_name,
                stream_arn=stream_arn,
                sampling_interval=sampling_interval,
                format_config=format_config,
                width_pixels=width_pixels,
                height_pixels=height_pixels,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("images",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    @contextmanager
    def get_media_for_fragment_list(
        self,
        fragments: "capo_kinesis_video_archived_media.types.fragment_number_list.FragmentNumberList",
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "Generator[capo_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput]":
        """<p>Gets media for a list of fragments (specified by fragment number) from the archived data in an Amazon Kinesis video stream.</p> <note> <p>You must first call the <code>GetDataEndpoint</code> API to get an endpoint. Then send the <code>GetMediaForFragmentList</code> requests to this endpoint using the <a href="https://docs.aws.amazon.com/cli/latest/reference/">--endpoint-url parameter</a>. </p> </note> <p>For limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p> <important> <p>If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: </p> <ul> <li> <p> <code>x-amz-ErrorType</code> HTTP header – contains a more specific error type in addition to what the HTTP status code provides. </p> </li> <li> <p> <code>x-amz-RequestId</code> HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.</p> </li> </ul> <p>Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.</p> <p>For more information, see the <b>Errors</b> section at the bottom of this topic, as well as <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html">Common Errors</a>. </p> </important>

        Args:
            stream_name: <p>The name of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamARN</code> parameter.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamName</code> parameter.</p>
            fragments: <p>A list of the numbers of fragments for which to retrieve media. You retrieve these values with <a>ListFragments</a>.</p>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.get_media_for_fragment_list_input.GetMediaForFragmentListInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.get_media_for_fragment_list_output.GetMediaForFragmentListOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_media_for_fragment_list

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.get_media_for_fragment_list.get_media_for_fragment_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.get_media_for_fragment_list_input.GetMediaForFragmentListInput = {
            "fragments": fragments
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_fragments(
        self,
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        max_results: Optional[
            "capo_kinesis_video_archived_media.types.list_fragments_max_results.ListFragmentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_kinesis_video_archived_media.types.next_token.NextToken"
        ] = None,
        fragment_selector: Optional[
            "capo_kinesis_video_archived_media.types.fragment_selector.FragmentSelector"
        ] = None,
    ) -> "capo_kinesis_video_archived_media.types.list_fragments_output.ListFragmentsOutput":
        """<p>Returns a list of <a>Fragment</a> objects from the specified stream and timestamp range within the archived data.</p> <p>Listing fragments is eventually consistent. This means that even if the producer receives an acknowledgment that a fragment is persisted, the result might not be returned immediately from a request to <code>ListFragments</code>. However, results are typically available in less than one second.</p> <note> <p>You must first call the <code>GetDataEndpoint</code> API to get an endpoint. Then send the <code>ListFragments</code> requests to this endpoint using the <a href="https://docs.aws.amazon.com/cli/latest/reference/">--endpoint-url parameter</a>. </p> </note> <important> <p>If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: </p> <ul> <li> <p> <code>x-amz-ErrorType</code> HTTP header – contains a more specific error type in addition to what the HTTP status code provides. </p> </li> <li> <p> <code>x-amz-RequestId</code> HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.</p> </li> </ul> <p>Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.</p> <p>For more information, see the <b>Errors</b> section at the bottom of this topic, as well as <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html">Common Errors</a>. </p> </important>

        Args:
            stream_name: <p>The name of the stream from which to retrieve a fragment list. Specify either this parameter or the <code>StreamARN</code> parameter.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream from which to retrieve a fragment list. Specify either this parameter or the <code>StreamName</code> parameter.</p>
            max_results: <p>The total number of fragments to return. If the total number of fragments available is more than the value specified in <code>max-results</code>, then a <a>ListFragmentsOutput$NextToken</a> is provided in the output that you can use to resume pagination.</p>
            next_token: <p>A token to specify where to start paginating. This is the <a>ListFragmentsOutput$NextToken</a> from a previously truncated response.</p>
            fragment_selector: <p>Describes the timestamp range and timestamp origin for the range of fragments to return.</p> <note> <p>This is only required when the <code>NextToken</code> isn't passed in the API.</p> </note>

        Raises:
            capo_kinesis_video_archived_media.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see <a href="http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html">Kinesis Video Streams Limits</a>.</p>
            capo_kinesis_video_archived_media.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used.</p>
            capo_kinesis_video_archived_media.errors.not_authorized_exception.NotAuthorizedException: <p>Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.</p>
            capo_kinesis_video_archived_media.errors.resource_not_found_exception.ResourceNotFoundException: <p> <code>GetImages</code> will throw this error when Kinesis Video Streams can't find the stream that you specified.</p> <p> <code>GetHLSStreamingSessionURL</code> and <code>GetDASHStreamingSessionURL</code> throw this error if a session with a <code>PlaybackMode</code> of <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>is requested for a stream that has no fragments within the requested time range, or if a session with a <code>PlaybackMode</code> of <code>LIVE</code> is requested for a stream that has no fragments within the last 30 seconds.</p>
            capo_kinesis_video_archived_media.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_video_archived_media.types.list_fragments_input.ListFragmentsInput]",
        ) -> OperationResponse[
            "capo_kinesis_video_archived_media.types.list_fragments_output.ListFragmentsOutput"
        ]:
            import capo_kinesis_video_archived_media._operations.aws_acuity_reader.list_fragments

            output, http_response = (
                capo_kinesis_video_archived_media._operations.aws_acuity_reader.list_fragments.list_fragments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_archived_media.types.list_fragments_input.ListFragmentsInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if fragment_selector is not None:
            input_["fragment_selector"] = fragment_selector

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_fragments(
        self,
        *,
        config_overrides: Optional[KinesisVideoArchivedMediaClientConfig] = None,
        stream_name: Optional[
            "capo_kinesis_video_archived_media.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
        ] = None,
        max_results: Optional[
            "capo_kinesis_video_archived_media.types.list_fragments_max_results.ListFragmentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_kinesis_video_archived_media.types.next_token.NextToken"
        ] = None,
        fragment_selector: Optional[
            "capo_kinesis_video_archived_media.types.fragment_selector.FragmentSelector"
        ] = None,
    ) -> "Iterator[capo_kinesis_video_archived_media.types.fragment.Fragment]":
        _token = next_token
        while True:
            _response = self.list_fragments(
                config_overrides=config_overrides,
                stream_name=stream_name,
                stream_arn=stream_arn,
                max_results=max_results,
                next_token=_token,
                fragment_selector=fragment_selector,
            )
            _page = _resolve_path(_response, ("fragments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
