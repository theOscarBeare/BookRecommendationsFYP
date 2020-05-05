import CustomPaginationActionsTable from './DataTable.jsx';
import Popup from 'reactjs-popup';
import SimilarRecommendationsActionsTable from './Similar Recommendations.jsx';
import SimilarToPreviousReadingsActionsTable from './Similar to previouse Readings.jsx';


class App extends Component {
  render() {
    return (
      <div className="recommendations">
          <div id="recommendations">
              <Card pageWrapId={"page-wrap"} outerContainerId={"recommendations"} />
                <header className="recommendations-header">
                    <h1 className="recommendations-title">Recommended Books</h1>
                </header>
              <div id="page-wrap">
                <body className="recommendations-intro">
                    Recommended Books Custom to YOU
                    <CustomPaginationActionsTable/>
                    <Popup modal trigger={<button>Recommendations</button>}>
                     <SimilarRecommendationsActionsTable/>
                    </Popup>
                <br>
                </br>
                Similar to what you have studied before
                <SimilarToPreviousReadingsActionsTable/>


                </body>
                <footer>Final Year Project</footer>
              </div>
          </div>
      </div>
    );
  }
}


export default recommendedBook;