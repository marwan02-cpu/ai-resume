'use client'

import {Button} from '@heroui/button';
function PrimaryButton({ getData }){
    return (
    <Button color="primary" className='self-center' onPress={getData}>
      Tailor resume
    </Button>
    )
}


export default PrimaryButton;