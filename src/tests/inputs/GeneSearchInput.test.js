import React from 'react';
import {configure, mount} from 'enzyme';
import {GeneSearchInput} from '../../inputs/GeneSearchInput'
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });

describe("GeneSearchInput", () => {
    let component;
    const handleTextChangeSpy = jest.fn();
    const handleSubmitSpy = jest.fn();

    beforeEach(() => {
        component = mount(
            <GeneSearchInput 
                handleTextChange={handleTextChangeSpy}
                handleSubmit={handleSubmitSpy}
            />
        )
    });

    it('should render the input bar', () => {
        expect(component.find("h5").text()).toContain("Query for your genes of interest here:");
    });
});