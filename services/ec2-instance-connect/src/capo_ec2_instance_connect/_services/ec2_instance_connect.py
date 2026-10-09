"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#AWSEC2InstanceConnectService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ec2_instance_connect._auth._signers
import capo_ec2_instance_connect._auth._sigv4
from capo_ec2_instance_connect._auth._identity import Credentials
from capo_ec2_instance_connect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ec2_instance_connect._auth._zapros_handler import AuthMiddleware
from capo_ec2_instance_connect._services._aws_config import aws_config
from capo_ec2_instance_connect._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.availability_zone
    import capo_ec2_instance_connect.types.instance_id
    import capo_ec2_instance_connect.types.instance_os_user
    import capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_request
    import capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_response
    import capo_ec2_instance_connect.types.send_ssh_public_key_request
    import capo_ec2_instance_connect.types.send_ssh_public_key_response
    import capo_ec2_instance_connect.types.serial_port
    import capo_ec2_instance_connect.types.ssh_public_key


class EC2InstanceConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class EC2InstanceConnectClient:
    """A client for the ``EC2InstanceConnect`` service.

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
        self._config = EC2InstanceConnectClientConfig(
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
        self, config_overrides: Optional[EC2InstanceConnectClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EC2InstanceConnectClientConfig = config_overrides or {}
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

    def send_serial_console_ssh_public_key(
        self,
        instance_id: "capo_ec2_instance_connect.types.instance_id.InstanceId",
        ssh_public_key: "capo_ec2_instance_connect.types.ssh_public_key.SSHPublicKey",
        *,
        config_overrides: Optional[EC2InstanceConnectClientConfig] = None,
        serial_port: Optional[
            "capo_ec2_instance_connect.types.serial_port.SerialPort"
        ] = None,
    ) -> "capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse":
        """<p>Pushes an SSH public key to the specified EC2 instance. The key remains for 60 seconds, which gives you 60 seconds to establish a serial console connection to the instance using SSH. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html">EC2 Serial Console</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            instance_id: <p>The ID of the EC2 instance.</p>
            serial_port: <p>The serial port of the EC2 instance. Currently only port 0 is supported.</p> <p>Default: 0</p>
            ssh_public_key: <p>The public key material. To use the public key, you must have the matching private key. For information about the supported key formats and lengths, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws">Requirements for key pairs</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Raises:
            capo_ec2_instance_connect.errors.auth_exception.AuthException: <p>Either your AWS credentials are not valid or you do not have access to the EC2 instance.</p>
            capo_ec2_instance_connect.errors.ec2_instance_not_found_exception.EC2InstanceNotFoundException: <p>The specified instance was not found.</p>
            capo_ec2_instance_connect.errors.ec2_instance_state_invalid_exception.EC2InstanceStateInvalidException: <p>Unable to connect because the instance is not in a valid state. Connecting to a stopped or terminated instance is not supported. If the instance is stopped, start your instance, and try to connect again.</p>
            capo_ec2_instance_connect.errors.ec2_instance_type_invalid_exception.EC2InstanceTypeInvalidException: <p>The instance type is not supported for connecting via the serial console. Only Nitro instance types are currently supported.</p>
            capo_ec2_instance_connect.errors.ec2_instance_unavailable_exception.EC2InstanceUnavailableException: <p>The instance is currently unavailable. Wait a few minutes and try again.</p>
            capo_ec2_instance_connect.errors.invalid_args_exception.InvalidArgsException: <p>One of the parameters is not valid.</p>
            capo_ec2_instance_connect.errors.serial_console_access_disabled_exception.SerialConsoleAccessDisabledException: <p>Your account is not authorized to use the EC2 Serial Console. To authorize your account, run the EnableSerialConsoleAccess API. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableSerialConsoleAccess.html">EnableSerialConsoleAccess</a> in the <i>Amazon EC2 API Reference</i>.</p>
            capo_ec2_instance_connect.errors.serial_console_session_limit_exceeded_exception.SerialConsoleSessionLimitExceededException: <p>The instance currently has 1 active serial console session. Only 1 session is supported at a time.</p>
            capo_ec2_instance_connect.errors.serial_console_session_unavailable_exception.SerialConsoleSessionUnavailableException: <p>Unable to start a serial console session. Please try again.</p>
            capo_ec2_instance_connect.errors.serial_console_session_unsupported_exception.SerialConsoleSessionUnsupportedException: <p>Your instance's BIOS version is unsupported for serial console connection. Reboot your instance to update its BIOS, and then try again to connect.</p>
            capo_ec2_instance_connect.errors.service_exception.ServiceException: <p>The service encountered an error. Follow the instructions in the error message and try again.</p>
            capo_ec2_instance_connect.errors.throttling_exception.ThrottlingException: <p>The requests were made too frequently and have been throttled. Wait a while and try again. To increase the limit on your request frequency, contact AWS Support.</p>
            capo_ec2_instance_connect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.SendSerialConsoleSSHPublicKeyRequest]",
        ) -> OperationResponse[
            "capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_response.SendSerialConsoleSSHPublicKeyResponse"
        ]:
            import capo_ec2_instance_connect._operations.awsec2_instance_connect_service.send_serial_console_ssh_public_key

            output, http_response = (
                capo_ec2_instance_connect._operations.awsec2_instance_connect_service.send_serial_console_ssh_public_key.send_serial_console_ssh_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ec2_instance_connect.types.send_serial_console_ssh_public_key_request.SendSerialConsoleSSHPublicKeyRequest = {
            "instance_id": instance_id,
            "ssh_public_key": ssh_public_key,
        }
        if serial_port is not None:
            input_["serial_port"] = serial_port

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_ssh_public_key(
        self,
        instance_id: "capo_ec2_instance_connect.types.instance_id.InstanceId",
        instance_os_user: "capo_ec2_instance_connect.types.instance_os_user.InstanceOSUser",
        ssh_public_key: "capo_ec2_instance_connect.types.ssh_public_key.SSHPublicKey",
        *,
        config_overrides: Optional[EC2InstanceConnectClientConfig] = None,
        availability_zone: Optional[
            "capo_ec2_instance_connect.types.availability_zone.AvailabilityZone"
        ] = None,
    ) -> "capo_ec2_instance_connect.types.send_ssh_public_key_response.SendSSHPublicKeyResponse":
        """<p>Pushes an SSH public key to the specified EC2 instance for use by the specified user. The key remains for 60 seconds. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html">Connect to your Linux instance using EC2 Instance Connect</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            instance_id: <p>The ID of the EC2 instance.</p>
            instance_os_user: <p>The OS user on the EC2 instance for whom the key can be used to authenticate.</p>
            ssh_public_key: <p>The public key material. To use the public key, you must have the matching private key.</p>
            availability_zone: <p>The Availability Zone in which the EC2 instance was launched.</p>

        Raises:
            capo_ec2_instance_connect.errors.auth_exception.AuthException: <p>Either your AWS credentials are not valid or you do not have access to the EC2 instance.</p>
            capo_ec2_instance_connect.errors.ec2_instance_not_found_exception.EC2InstanceNotFoundException: <p>The specified instance was not found.</p>
            capo_ec2_instance_connect.errors.ec2_instance_state_invalid_exception.EC2InstanceStateInvalidException: <p>Unable to connect because the instance is not in a valid state. Connecting to a stopped or terminated instance is not supported. If the instance is stopped, start your instance, and try to connect again.</p>
            capo_ec2_instance_connect.errors.ec2_instance_unavailable_exception.EC2InstanceUnavailableException: <p>The instance is currently unavailable. Wait a few minutes and try again.</p>
            capo_ec2_instance_connect.errors.invalid_args_exception.InvalidArgsException: <p>One of the parameters is not valid.</p>
            capo_ec2_instance_connect.errors.service_exception.ServiceException: <p>The service encountered an error. Follow the instructions in the error message and try again.</p>
            capo_ec2_instance_connect.errors.throttling_exception.ThrottlingException: <p>The requests were made too frequently and have been throttled. Wait a while and try again. To increase the limit on your request frequency, contact AWS Support.</p>
            capo_ec2_instance_connect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To push an SSH key to an EC2 instance
            The following example pushes a sample SSH public key to the EC2 instance i-abcd1234 in AZ us-west-2b for use by the instance OS user ec2-user.

            >>> client.send_ssh_public_key(instance_id='i-abcd1234', instance_os_user='ec2-user', ssh_public_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3FlHqj2eqCdrGHuA6dRjfZXQ4HX5lXEIRHaNbxEwE5Te7xNF7StwhrDtiV7IdT5fDqbRyGw/szPj3xGkNTVoElCZ2dDFb2qYZ1WLIpZwj/UhO9l2mgfjR56UojjQut5Jvn2KZ1OcyrNO0J83kCaJCV7JoVbXY79FBMUccYNY45zmv9+1FMCfY6i2jdIhwR6+yLk8oubL8lIPyq7X+6b9S0yKCkB7Peml1DvghlybpAIUrC9vofHt6XP4V1i0bImw1IlljQS+DUmULRFSccATDscCX9ajnj7Crhm0HAZC0tBPXpFdHkPwL3yzYo546SCS9LKEwz62ymxxbL9k7h09t', availability_zone='us-west-2a')
        """

        def _handler(
            req: "OperationRequest[capo_ec2_instance_connect.types.send_ssh_public_key_request.SendSSHPublicKeyRequest]",
        ) -> OperationResponse[
            "capo_ec2_instance_connect.types.send_ssh_public_key_response.SendSSHPublicKeyResponse"
        ]:
            import capo_ec2_instance_connect._operations.awsec2_instance_connect_service.send_ssh_public_key

            output, http_response = (
                capo_ec2_instance_connect._operations.awsec2_instance_connect_service.send_ssh_public_key.send_ssh_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ec2_instance_connect.types.send_ssh_public_key_request.SendSSHPublicKeyRequest = {
            "instance_id": instance_id,
            "instance_os_user": instance_os_user,
            "ssh_public_key": ssh_public_key,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
