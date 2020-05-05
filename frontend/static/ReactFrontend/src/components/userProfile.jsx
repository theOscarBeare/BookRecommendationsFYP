import CustomPaginationActionsTable from './DataTable.jsx';
import Popup from 'reactjs-popup';
import SimilarRecommendationsActionsTable from './Similar Recommendations.jsx';
import userProfileTable from './userProfileTable.jsx';


class App extends Component {
  render() {
    return (
      <div className="userProfile">
          <div id="userProfile">
              <Card pageWrapId={"page-wrap"} outerContainerId={"userProfile"} />
                <header className="userProfile-header">
                    <h1 className="userProfile-title">User Profile</h1>
                </header>
              <div id="page-wrap">
                <body className="userProfile-intro">
                    Featured Books of the day
                    <userProfileTable/>
                </body>
                <footer>Final Year Project</footer>
              </div>
          </div>
      </div>
    );
  }
}


export default userProfile;