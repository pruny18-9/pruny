import React, { Component } from "react";
import './ItemCreateView.css';


class ItemCreateView extends Component{
    constructor(props){
        super(props)

        this.state={
            item_name:"",
            item_img:""
        }
    }

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value,
        });
    }

    itemCreate() {
        if (this.state.item_name != ""){
            this.props.itemCreate(this.state.item_name, this.state.item_img)
            this.setState({
                item_name: "",
                item_img: ""
            })
        } else {
            alert("이름 입력은 필수입니다.")
        }   
    }

    render(){
        const {} = this.state

        return(
            <div className='ItemCreateOption'>
                <div className="ItemCreateView">
                    <div>
                        <p>*이름</p>
                        <input name="item_name" onChange={this.handleChange} value={this.state.item_name}></input>
                    </div>
                    <div>
                        <p>사진</p>
                        <input name="item_img" onChange={this.handleChange} value={this.state.item_img}></input>
                    </div>
                    <button className="itemCreateBtn" onClick={() => this.itemCreate()}>생성</button>
                </div>
            </div>
        )
        
    }
}

export default ItemCreateView