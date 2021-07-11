import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "./App.css";

// geojson importing test
import CarMap from './components/carmap';

function App() {
  return (
    // Commented this out for components

    // This is a test of Leaflet, this will be moved into it's own component
    // <MapContainer center={[51.505, -0.09]} zoom={13}>
    //   { <TileLayer
    //     attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    //     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    //   /> }
      
    //   <Marker position={[51.505, -0.09]}>
    //       <Popup>
    //         A pretty CSS3 popup. <br /> Easily customizable.
    //       </Popup>
    //   </Marker>
    // </MapContainer>,
    
    <CarMap/>
  );
}

export default App;
