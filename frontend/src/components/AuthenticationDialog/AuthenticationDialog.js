import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import './AuthenticationDialog.scss';
import { authenticate } from '../../actions';
import { VALID_PARTICIPANT_IDS } from './participant-ids';

/**
 * Checks if the passed id is in the list of valid participant ids.
 * @param id
 * @returns {boolean}
 */
const isValidParticipantId = (id) => {
  if (id == null || id === '') {
    return false;
  }

  return VALID_PARTICIPANT_IDS.indexOf(id.toUpperCase()) > -1;
};

class AuthenticationDialog extends Component {
  static propTypes = {
    authenticated: PropTypes.bool,
    authenticationEnabled: PropTypes.bool,
    onAuthentication: PropTypes.func,
  };

  static defaultProps = {
    onAuthentication: (participantId) => {},
    authenticated: false,
    authenticationEnabled: false,
  };

  constructor(props) {
    super(props);

    this.state = {
      invalidParticipantId: false,
      participantId: '',
    };

    // Allows accessing the DOM element
    this.participantIdRef = React.createRef();
  }

  /**
   * Checks whether a dash should be added to the input.
   * They are added on the fourth and 8th position.
   * XXX-XXX-XXX
   */
  addDash = () => {
    let participantId = this.participantIdRef.current.value;

    if (participantId != null && participantId > this.state.participantId) {
      if (participantId.length === 3 || participantId.length === 7) {
        // Automatically adds dashes at these positions
        participantId = `${participantId}-`;
        this.participantIdRef.current.value = participantId;
      }
    }

    // Set the current value
    this.setState({ participantId });
  };

  /**
   * Checks whether the code is valid,
   * before authenticating the participant
   */
  authenticate = () => {
    const { onAuthentication } = this.props;
    const participantId = this.participantIdRef.current.value;

    if (isValidParticipantId(participantId)) {
      this.setState({
        invalidParticipantId: false,
      });

      // Dispatch to the store
      onAuthentication(participantId);
    } else {
      this.setState({
        invalidParticipantId: true,
      });
    }
  };

  render() {
    const { authenticated, authenticationEnabled } = this.props;
    const { invalidParticipantId } = this.state;
    const showAuthentication = authenticationEnabled && !authenticated;

    return (
      <Dialog open={showAuthentication} className="authentication-dialog">
        <DialogTitle>Authentication</DialogTitle>
        <DialogContent>
          <DialogContentText className="authentication-dialog__description">
            In order to chat with the bot, you will have to enter your Participant ID.
          </DialogContentText>
          <TextField
            autoFocus
            id="participantId"
            label="Participant ID"
            onChange={this.addDash}
            inputProps={{ maxLength: 11 }}
            type="text"
            required
            error={invalidParticipantId}
            helperText={invalidParticipantId ? 'Invalid' : ''}
            inputRef={this.participantIdRef}
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={this.authenticate}>
            Authenticate
          </Button>
        </DialogActions>
      </Dialog>
    );
  }
}

/**
 * Creates the mapping to the Redux store
 * @param state
 * @returns {{messages: (*|*[])}}
 */
function mapStateToProps(state) {
  return {
    authenticated: state.behavior.authenticated,
    authenticationEnabled: state.behavior.authenticationEnabled,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    onAuthentication: (participantId) => {
      dispatch(authenticate(participantId));
    },
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(AuthenticationDialog);
