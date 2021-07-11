import React, { Component } from 'react'
import mapData from './../data/mygeodata_merged.json'
import 'leaflet/dist/leaflet.css'
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
class CarMap extends Component {
    state = {};

componentDidMount(){
    console.log(mapData)
}

    render() {
        return (
            <div>
                <h1 style={{textAlign:'center'}}> Test Map </h1>
                <MapContainer style={{height:'80vh'}} zoom={5} center={[53.969332176238993, -103.912761888850071]}>
                    {<TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    /> }    
                    <GeoJSON data={mapData.features}/>
                </MapContainer>

            </div>
        )
    }
}

export default CarMap