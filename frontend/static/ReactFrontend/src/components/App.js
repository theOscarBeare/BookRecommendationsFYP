import React, { Component } from 'react';
import './App.css';
import Card from './DropDown.js';
import CustomPaginationActionsTable from './DataTable.jsx';
import Popup from 'reactjs-popup';
import SimilarRecommendationsActionsTable from './Similar Recommendations.jsx';
import SimilarToPreviousReadingsActionsTable from './Similar to previouse Readings.jsx';


class App extends Component {
  render() {
    return (
      <div className="App">
          <div id="App">
              <Card pageWrapId={"page-wrap"} outerContainerId={"App"} />
                <header className="App-header">
                    <h1 className="App-title">Welcome to Book Recommendations</h1>
                </header>
              <div id="page-wrap">
                <body className="App-intro">
                    Featured Books of the day
                    <CustomPaginationActionsTable/>
                    <Popup modal trigger={<button>Similar Recommendations</button>}>
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


export default App;