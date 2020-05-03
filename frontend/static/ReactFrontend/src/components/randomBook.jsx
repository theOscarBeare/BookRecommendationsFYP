import CustomPaginationActionsTable from './DataTable.jsx';
import Popup from 'reactjs-popup';
import SimilarRecommendationsActionsTable from './Similar Recommendations.jsx';
import SimilarToPreviousReadingsActionsTable from './Similar to previouse Readings.jsx';


class App extends Component {
  render() {
    return (
      <div className="randomBook">
          <div id="randomBook">
              <Card pageWrapId={"page-wrap"} outerContainerId={"randomBook"} />
                <header className="randomBook-header">
                    <h1 className="randomBook-title">Welcome to Book Recommendations</h1>
                </header>
              <div id="page-wrap">
                <body className="randomBook-intro">
                    Fancy Reading a New Book?
                    <CustomPaginationActionsTable/>
                    <Popup modal trigger={<button>Recommendations</button>}>
                     <SimilarRecommendationsActionsTable/>
                    </Popup>
                </body>
                <footer>Final Year Project</footer>
              </div>
          </div>
      </div>
    );
  }
}


export default randomBook;